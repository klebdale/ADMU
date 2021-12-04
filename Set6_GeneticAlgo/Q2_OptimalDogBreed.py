"""
    Bayaras, Kleb Dale G.
    217095
"""
from numpy.random import randint
from numpy.random import rand
import random
import itertools

"""
1) Randomly initialize population p
2) Determine fitness of population
3) Until convergence repeat:
      a) Select parents from population
      b) Crossover and generate new population
      c) Perform mutation on new population
      d) Calculate fitness for new population
"""
"""
    Optimal Dog Breeds - maximization
    Gene =  breed(string), weight(float 0-100), body_fat(float 0-1), is_vacc(bool), 
            has_won(bool), age(int), inteliigence(float 0-3)
    Chromosome/Dog = list form of attributes i.e. ["Corgi", 45.1, 0.33, True, False, 3, 101]
    Solution = pair of dogs
    Population building = Have initial list of dogs and then pair them up?
    i.e.    A = ['BorderCollie', 45.11116148940769, 0.3534805164826734, 1, 1, 5, 0.5070958741415176]
            Dogs = [A, B, C, D]
            Population = [[A,B], [A,C], [A,D], [B,C], [B,D], [C,D]]
    
    Fitness Function:
        Poor = -1, Average = 0, Good = 1, Excellent = 2
        
        1.  If breed1 != breed2, score += 0; else score += 1
        2.  If weight < 40, score += -1
            If 40 <= weight <= 80, score += 1
            If weight > 80, score += 0
        3.  If 0 <= body_fat <= 0.25, score += 2
            If 0.25 < body_fat <= 0.75, score += 0
            If body_fat > 0.75, score += -1
        4.  If (has_won) and (40 <= weight <= 80), score += 1
            else score += 0
        5.  If age in (1,2), score += 0
            If age == 3, score += 1
            If age in (4,5)
                If has_won, score += -1
                else score += -2
        6.  If is_vacc, score += 1
        7.  score += ave(intelligence)
"""


# Modularize functions for fitness function
def weight_scoring(dog):
    if dog[1] < 40.00:
        return -1
    elif 40.00 <= dog[1] <= 80.00:
        return 1
    elif dog[1] > 80.00:
        return 0


def body_fat_scoring(dog):
    if 0 <= dog[2] <= 0.25:
        return 2
    elif 0.25 < dog[2] <= 0.75:
        return 0
    elif dog[2] > 0.75:
        return -1


def is_vacc_scoring(dog):
    if dog[3] == 1:
        return 1
    else:
        return -1


def has_won_scoring(dog):
    if (dog[4] == 1) and (40.00 <= dog[1] <= 80.00):
        return 1
    else:
        return 0


def age_scoring(dog):
    if dog[5] in (1, 2):
        return 0

    elif dog[5] == 3:
        return 1

    elif dog[5] in (4, 5):
        if dog[4] == 1:
            return -1
        else:
            return -2


# Objective function. Theoretical Max = 16 (based on the input limits)
def fitness_function(pair):
    score = 0.0
    dog1 = pair[0]
    dog2 = pair[1]
    # Breed
    if dog1[0] == dog2[0]:
        score += 1
    # Weight (-1, 0, 1)
    score += weight_scoring(dog1)
    score += weight_scoring(dog2)
    # Body fat (-1, 0, 2)
    score += body_fat_scoring(dog1)
    score += body_fat_scoring(dog2)
    # Is vaccinated (1 or -1)
    score += is_vacc_scoring(dog1)
    score += is_vacc_scoring(dog2)
    # Has won (0 or 1)
    score += has_won_scoring(dog1)
    score += has_won_scoring(dog2)
    # Age
    score += age_scoring(dog1)
    score += age_scoring(dog2)
    # Intelligence
    score += (dog1[6] + dog2[6]) / 2

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
def crossover(pair1, pair2, probability_crossover):
    # Children are copies of parents by default. Format each child is [A,B]
    child1, child2 = pair1.copy(), pair2.copy()
    if rand() <= probability_crossover:
        # select a crossover point that is not at the end of the string
        pt = randint(1, len(pair1[0]) - 2)
        # perform crossover
        child1 = pair1[0][:pt] + pair2[1][pt:], pair2[1][:pt] + pair1[0][pt:]
        child2 = pair2[0][:pt] + pair1[1][pt:], pair1[1][:pt] + pair2[0][pt:]
    return [list(child1), list(child2)]


# Mutation
def mutation(gene, probability_mutation):
    for i in range(len(gene[0])):
        # Check for a mutation
        if rand() <= probability_mutation:
            # Breed
            if i == 0:
                gene[0][i] = random.choice(breeds)
                gene[1][i] = random.choice(breeds)
            # Weight
            if i == 1:
                gene[0][i] = random.uniform(0, 100)
                gene[1][i] = random.uniform(0, 100)
            # Body Fat
            if i == 2:
                gene[0][i] = random.uniform(0, 1)
                gene[1][i] = random.uniform(0, 1)
            # Vaccinated & Won Award
            if i in (3, 4):
                gene[0][i] = random.getrandbits(1)
                gene[1][i] = random.getrandbits(1)
            # Age
            if i == 5:
                gene[0][i] = random.randint(1, 5)
                gene[1][i] = random.randint(1, 5)
            # Intelligence
            if i == 6:
                gene[0][i] = random.uniform(0, 3)
                gene[1][i] = random.uniform(0, 3)


"""
Gene =  breed(string), weight(float 0-100), body_fat(float 0-1), is_vacc(bool), 
            has_won(bool), age(int 0-5), intelligence(float 0-3)
    Note: True = 1, False = 0
"""

# Setup
breeds = ['Corgi', 'Husky', 'Shiba', 'Malamute', 'BorderCollie', 'GermanShepherd']
n_dogs = 12 #n_dogs should be yield an even number of combination pairs
n_iter = 1000
probability_crossover = 0.75
probability_mutation = 0.5
population = []

# Create Dogs
dogs = [[random.choice(breeds), random.uniform(0, 100), random.uniform(0, 1), random.getrandbits(1),
         random.getrandbits(1), random.randint(1, 5), random.uniform(0, 3)] for _ in range(n_dogs)]

# Pair them up and append to population list
for pair in itertools.combinations(dogs, 2):
    population.append(list(pair))

# Population Format [[[],[]]]
n_pop = len(population)

# Keep track of the best solution
best_score, best_gene = fitness_function(population[0]), population[0]

for gen in range(n_iter):
    print("Generation {}".format(gen))

    # Evaluation
    scores = [fitness_function(c) for c in population]

    # Check for the new best solution
    found = False
    for i in range(len(population)):
        if scores[i] > best_score:
            best_score, best_gene = scores[i], population[i]
            print("New Best [Score, Pair]: {} {}".format(best_score, best_gene))
            found = True
    if not found:
        print("Still Best [Score, Pair]: {} {}".format(best_score, best_gene))

    # Select parents
    parents = [selection(population, scores) for _ in range(n_pop)]

    # Create the next generation
    children = list()
    for i in range(0, n_pop, 2):
        # Get selected parents
        pair1, pair2 = parents[i], parents[i + 1]
        # Crossover and mutation
        for child in crossover(pair1, pair2, probability_crossover):
            # Mutation
            mutation(child, probability_mutation)
            # Store for the next generation
            children.append(child)
    # Replace the population
    population = children

print("Timeline over...")
print("Best Pair: {}".format(best_gene))
print("Score: {}".format(best_score))
