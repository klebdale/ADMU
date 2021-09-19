import numpy as np

## Step 0
# Inputs and Labels
x = [
    [0.2, 0.48, 0.46, 0],
    [0.45, 0.04, 0.09, 0],
    [0.08, 0.41, 0.17, 0],
    [0.02, 0.05, 0.04, 0],
    [0.02, 0.35, 0.28, 0],
    [0.29, 0.21, 0.35, 0],
    [0.43, 0.27, 0.08, 0],
    [0.03, 0.49, 0.5, 0],
    [0.32, 0.18, 0.08, 0],
    [0.05, 0.03, 0.23, 0],
    [0.67, 0.7, 0.88, 1],
    [1, 0.78, 0.9, 1],
    [0.58, 0.57, 0.96, 1],
    [0.51, 0.85, 0.9, 1],
    [0.76, 0.76, 0.81, 1],
    [0.77, 0.87, 0.89, 1],
    [0.81, 0.86, 0.79, 1],
    [0.64, 0.89, 0.97, 1],
    [0.94, 0.56, 0.9, 1],
    [0.6, 0.75, 0.95, 1],
    [0.94, 0.62, 0.83, 1]
]

# Initial Weights
weight = [0.5, 0.13, 0.21, 0.1]
bias = 1


# Training function
def training_spa(max_iter, x):
    ## Step 1 - Initilization of variables

    # Learning Rate
    learning_rate = 0.01

    # Step Function
    prediction = 0

    # Diff
    diff = 0

    # Max Iterations
    max_iterations = max_iter

    # MSE dict
    mse = {}

    ## Step 2 - Loop and compute
    for iteration in range(1, max_iterations + 1):
        sum_mse = 0
        print("\n--------------------- Iteration Number " +str(iteration)+" ---------------------\n")

        # Send all data points into the computation
        # i is each datapoint (or row in the spreadsheet)
        for i in range(0, len(x)):
            sum = 0

            # weighted_sum, -1 since last index is the label
            # j is each value in the datapoint (or xN in the spreadsheet)
            for j in range(0, len(x[i]) - 1):
                sum += x[i][j] * weight[j]

            # Output = Bias + Weighted_sum
            # Output is the Signal
            output = sum + (bias * weight[-1])

            # Apply Activation on Output
            # Activation Function is the Prediction in spreadsheet
            # Activation Function = 1/(1+EXP(-Signal))
            prediction = 1 / (1 + np.exp(-output))

            # Compare expected label to prediction then calculate diff
            diff = (prediction - x[i][-1]) ** 2

            sum_mse += diff

            print("---> Data Point #",i,
                 "\nInput:", x[i],
                 " Weights:", weight,
                 "\nOutput Sum:", output,
                 " Prediction:", prediction,
                 " Diff: ", diff)

            # Update weights
            for j in range(0, len(weight) - 1):
                weight[j] = weight[j] + (learning_rate * (x[i][-1] - prediction) * x[i][j])

            # Weight of Bias Update
            weight[-1] = weight[-1] + (learning_rate * (x[i][-1] - prediction) * bias)

            answer = "New Weights are: "+str(weight)
            print(answer+"\n")

        # print("MSE for Iteration Number "+str(iteration)+" is:", sum_mse/len(x))

        mse[iteration] = sum_mse / len(x)

    print("MSE Trend:")
    for key in mse:
        print('Iter #',key, ':', mse[key])
        #print(mse[key])
    print("\nDone!\n")
    return weight

    ###END DEF of training_spa###


def test_spa(x_input, weight):
    threshold = 0.5
    sum = 0

    for i in range(0, len(x_input)):
        for j in range(0, len(x_input[i])):
            sum += x_input[i][j] * weight[j]

        output = sum + (bias * weight[-1])
        prediction = 1 / (1 + np.exp(-output))

        if prediction >= threshold:
            x_input[i].append(1)
        else:
            x_input[i].append(0)

        print("Dataset " + str(x_input[i][:-1]) + " Label is: " + str(x_input[i][-1]))

    ###END DEF of test_spa###


max_iter = 0
x_input = []
sublist = []

max_iter = int(input("Input maximum iterations:"))
n = int(input("Enter Number of Datasets to Predict: "))

for i in range(0, n):
    sublist = [float(item) for item in input("Enter Dataset #" + str(i + 1) + " space-separated:").split()]
    x_input.append(sublist)

test_spa(x_input, training_spa(max_iter, x))

