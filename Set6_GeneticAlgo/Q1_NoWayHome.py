"""
    Bayaras, Kleb Dale G.
    217095
"""
from numpy.random import randint
from numpy.random import rand
import math

"""
1) Randomly initialize populations p
2) Determine fitness of population
3) Until convergence repeat:
      a) Select parents from population
      b) Crossover and generate new population
      c) Perform mutation on new population
      d) Calculate fitness for new population

    NoWayHome - Minimization
    Gene = 3d coordinate (x,y,z)
    Chromosome = 10 Genes
    Individual Solution is 10 multiples of 3d coordinates [[x0,y0,z0],...,[x9,y9,z9]]
    Target = Oscorp (Also a 3d coordinate)

    Fitness Function:
        Summation of distances of each gene
        d(gene[0], gene[1]) + d(gene[1], gene[2]) + ... + d(gene[8], gene[9])

        #Constraints
        Tree = +5 units
        Bldg = +11 units
        Vlln = *2 of the distance segment
"""


# Distance Formula
def calc_distance(c1, c2):
    distance = math.sqrt(((c2[0] - c1[0]) ** 2) + ((c2[1] - c1[1]) ** 2) + ((c2[2] - c1[2]) ** 2))
    return distance


# Is point in between swing locations?
# ref: https://math.stackexchange.com/questions/3210769/how-do-i-check-if-a-3d-point-is-between-2-other-3d-points/3210790
def is_between(c1, c2, obstruction_list):
    for obstruction in obstruction_list:
        try:
            x_thing = (obstruction[0] - c1[0]) / (c2[0] - c1[0])
        except ZeroDivisionError:
            x_thing = 0
        try:
            y_thing = (obstruction[1] - c1[1]) / (c2[1] - c1[1])
        except ZeroDivisionError:
            y_thing = 0
        try:
            z_thing = (obstruction[2] - c1[2]) / (c2[2] - c1[2])
        except ZeroDivisionError:
            z_thing = 0

        if x_thing == y_thing == z_thing:
            return True
    return False


# Objective function
def fitness_function(solution, target_coord):
    score = 0

    """ Original / No constraints
    for i in range(len(solution) - 1):
        score += calc_distance(solution[i], solution[i + 1])
    # Calculate distance of last coordinate with the target coordinate and add it
    score += calc_distance(solution[-1], target_coord)
    return score
    """
    for i in range(len(solution) - 1):
        if is_between(solution[i], solution[i + 1], vllns):
            score += (calc_distance(solution[i], solution[i + 1]) * 2)
            # print("Villain Encountered")

        elif is_between(solution[i], solution[i + 1], bldgs):
            score += calc_distance(solution[i], solution[i + 1])
            score += 11
            # print("Building Encountered")

        elif is_between(solution[i], solution[i + 1], trees):
            score += calc_distance(solution[i], solution[i + 1])
            score += 5
            # print("Tree Encountered")

        else:
            score += calc_distance(solution[i], solution[i + 1])

    # Calculate distance of last coordinate with the target coordinate and add it
    score += calc_distance(solution[-1], target_coord)
    return score


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
def crossover(parent1, parent2, prob_crossover):
    # Children are copies of parents by default
    child1, child2 = parent1.copy(), parent2.copy()

    if rand() < prob_crossover:
        # select a crossover point that is not at the end of the string
        pt = randint(1, len(parent1) - 2)
        # perform crossover
        child1 = parent1[:pt] + parent2[pt:]
        child2 = parent2[:pt] + parent1[pt:]
    return [child1, child2]


# Mutation
def mutation(gene, prob_mutation):
    for i in range(len(gene)):
        # Check for a mutation
        if rand() < prob_mutation:
            # random number between 0 - 100
            gene[i] = randint(0, 100, n_dim).tolist()


# Setup
n_pop = 100  # Population
n_swings = 10  # Spidey Swings
n_dim = 3  # x,y,z
n_iter = 100  # Number of Generations
target_coord = [10, 10, 20]  # Oscorp
prob_crossover = 0.5
prob_mutation = 0.25

# Obstacle Random Coordinates
n_trees = 100
n_bldgs = 100
n_vllns = 100
trees = [randint(0, 100, n_dim).tolist() for _ in range(n_trees)]
bldgs = [randint(0, 100, n_dim).tolist() for _ in range(n_bldgs)]
vllns = [randint(0, 100, n_dim).tolist() for _ in range(n_vllns)]
# print(trees, "\n", bldgs, "\n", vllns)

# Initial Population | Format:[[[]]] Population of Chromosomes of Genes
population = [[randint(0, 100, n_dim).tolist() for _ in range(n_swings)] for __ in range(n_pop)]

# Keep track of the best solution
best_score, best_gene = 100000, fitness_function(population[0], target_coord)

# Choice of (a) limited number of iterations or (b) iterate until best_score is below a certain number
# for gen in range(n_iter):
gen = 0
while best_score > 300:
    print("Generation {}".format(gen))

    # Evaluation
    scores = [fitness_function(c, target_coord) for c in population]

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
        for child in crossover(parent1, parent2, prob_crossover):
            # Mutation
            mutation(child, prob_mutation)
            # Store for the next generation
            children.append(child)
    # Replace the population
    population = children
    print(population)
    gen += 1

print("Timeline over...")
best_gene.append(target_coord)
print("Best Path: {}".format(best_gene))
print("Total Distance: {}".format(best_score))
