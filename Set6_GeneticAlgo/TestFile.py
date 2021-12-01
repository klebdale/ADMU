from numpy.random import randint
from numpy.random import rand
"""
1) Randomly initialize populations p
2) Determine fitness of population
3) Until convergence repeat:
      a) Select parents from population
      b) Crossover and generate new population
      c) Perform mutation on new population
      d) Calculate fitness for new population
"""


# Objective function
def fitness_function(solution):
    return sum(solution)


# Selection by tournament
def selection(population, scores, k=2):
    # Random selection
    selected_index = randint(len(population))
    for i in randint(0, len(population), k - 1):
        # Check the best performing
        if scores[i] < scores[selected_index]:
            selected_index = i
    return population[selected_index]


# Crossover
def crossover(parent1, parent2, probability_crossover):
    # Children are copies of parents by default
    child1, child2 = parent1.copy(), parent2.copy()
    if rand() < probability_crossover:
        # select a crossover point that is not at the end of the string
        pt = randint(1, len(parent1) - 2)
        # perform crossover
        child1 = parent1[:pt] + parent2[pt:]
        child2 = parent2[:pt] + parent1[pt:]
    return [child1, child2]


# Mutation
def mutation(gene, probability_mutation):
    for i in range(len(gene)):
        # Check for a mutation
        if rand() < probability_mutation:
            # flip the bit
            gene[i] = 1 - gene[i]


n_pop = 1000
n_bits = 6
n_iter = 10
probability_crossover = 0.5
probability_mutation = 0.5
population = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]

# Keep track of the best solution
best_score, best_gene = 100000, fitness_function(population[0])

for gen in range(n_iter):
    print("Generation {}".format(gen))
    # Evaluation
    scores = [fitness_function(c) for c in population]
    # Check for the new best solution
    found = False
    for i in range(len(population)):
        if scores[i] < best_score:
            best_score, best_gene = scores[i], population[i]
            print("{} new best with score {}".format(best_gene, best_score))
            found = True
    if not found:
        print("{} still the best with score {}".format(best_gene, best_score))
    # Select parents
    parents = [selection(population, scores) for _ in range(n_pop)]
    # Create the next generation
    children = list()
    for i in range(0, n_pop, 2):
        # Get selected parents
        parent1, parent2 = parents[i], parents[i + 1]
        # Crossover and mutation
        for child in crossover(parent1, parent2, probability_crossover):
            # Mutation
            mutation(child, probability_mutation)
            # Store for the next generation
            children.append(child)
    # Replace the population
    population = children
print("Timeline over...")
print("Best Gene: {}".format(best_gene))
print("Score: {}".format(best_score))
