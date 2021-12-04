"""
    Bayaras, Kleb Dale G.
    217095
"""
from numpy.random import randint
from numpy.random import rand
import numpy as np
import cv2
from PIL import Image as im

"""
1) Randomly initialize populations p
2) Determine fitness of population
3) Until convergence repeat:
      a) Select parents from population
      b) Crossover and generate new population
      c) Perform mutation on new population
      d) Calculate fitness for new population
"""
"""
    Mona Lisa BnW - Minimization
    Gene = each cell in the matrix
    Chromosome = A matrix of mxm (reduced dimension)
    Population = list of mxm matrices

    Fitness Function:
        difference = (cell of ideal - cell of random)**2 
        add the differences after all cells are computed.
        So, if there are 64x64 cells, get the difference of the same coordinates and sum it all up
        The closer to 0, the better
"""


# Objective function
def fitness_function(random_matrix):
    score = 0
    # TODO: Optimize for faster runtime
    for row in range(0, m):
        for col in range(0, m):
            difference = (ideal_reduced_matrix[row][col] - random_matrix[row][col]) ** 2
            score += difference

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
def crossover(parent1, parent2, probability_crossover):
    # Children are copies of parents by default. each child is a matrix
    child1, child2 = parent1.copy(), parent2.copy()
    if rand() < probability_crossover:
        # Swap the rows
        pt = randint(1, m - 2)
        # perform crossover
        child1 = np.concatenate((parent1[:pt], parent2[pt:]))
        child2 = np.concatenate((parent2[:pt], parent1[pt:]))
    return [child1, child2]


# Mutation
def mutation(gene, probability_mutation):
    for i in range(m):
        for j in range(m):
            # Check for a mutation
            if rand() < probability_mutation:
                gene[i][j] = abs(1 - gene[i][j])


def pic_to_float_array(img_path):
    img = cv2.imread(img_path, 0)  # read image as grayscale. Set second parameter to 1 if rgb is required
    new_img = img / 255.0
    return np.array(new_img)


def array_to_bw_pic(matrix, new_img_path):
    my_array = (matrix * 255).astype(np.uint8)
    img_new = im.fromarray(my_array)
    img_new.save(new_img_path)


# Setup for getting ideal matrix
n = 256  # Dimension of Original Matrix (nxn)
m = 64  # Dimension of Reduced Matrix (mxm)
pics_file_path = '/Users/kleb/Desktop/GA_Pics/'
np.set_printoptions(precision=2, suppress=True)  # Printing of floating point precisions

orig_matrix = pic_to_float_array(pics_file_path + '1_monalisa_orig.jpg')
array_to_bw_pic(orig_matrix, pics_file_path + '2_monalisa_bw.png')

# Averaging to get the ideal matrix
ave_list = []
skip = 4
for row in range(0, n - 1, skip):
    for col in range(0, n - 1, skip):
        ave_amt = orig_matrix[row][col] + orig_matrix[row][col + 1] + orig_matrix[row][col + 2] + orig_matrix[row][
            col + 3]
        ave_amt += orig_matrix[row + 1][col] + orig_matrix[row + 1][col + 1] + orig_matrix[row + 1][col + 2] + \
                   orig_matrix[row + 1][col + 3]
        ave_amt += orig_matrix[row + 2][col] + orig_matrix[row + 2][col + 1] + orig_matrix[row + 2][col + 2] + \
                   orig_matrix[row + 1][col + 3]
        ave_amt += orig_matrix[row + 3][col] + orig_matrix[row + 3][col + 1] + orig_matrix[row + 3][col + 2] + \
                   orig_matrix[row + 1][col + 3]

        ave_list.append(ave_amt / (skip ** 2))

ideal_reduced_matrix = np.reshape(ave_list, (m, m))
array_to_bw_pic(ideal_reduced_matrix, pics_file_path + '3_monalisa_bw_reduced.png')

# GA starts here
n_pop = 50
n_iter = 2000
probability_crossover = 0.5
probability_mutation = 0.3

# Create a list of n_pop mxm matrices with random floating values (0-1)
population = [np.random.random((m, m)) for _ in range(n_pop)]
# Keep track of the best solution
best_score, best_matrix = 100000, population[0]

for gen in range(n_iter):
    # gen = 0
    # while(best_score > 520):
    #    gen+=1
    print("Generation {}".format(gen))

    # Evaluation
    scores = [fitness_function(c) for c in population]

    # Check for the new best solution
    found = False
    for i in range(len(population)):
        if scores[i] < best_score:
            best_score, best_matrix = scores[i], population[i]
            print("{} new best with score {}".format(best_matrix, best_score))
            found = True
    if not found:
        pass
        # print("{} still the best with score {}".format(best_matrix, best_score))

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
print("Ideal Gene: {}".format(ideal_reduced_matrix))
print("Best Gene: {}".format(best_matrix))
print("Score: {}".format(best_score))
array_to_bw_pic(best_matrix, pics_file_path + '4_monalisa_ga_result.png')
"""
    I tried converting the best_matrix into a reduced resolution photo but all I get is a noisy photo,
    akin to a TV without a signal. I'll attach a screenshot of the photos that attempted to GA its way.
    I think I need a better crossover and mutation function
"""
