## Step 0
#Inputs and Labels
x = [
    [0.72,0.82,-1],
    [0.91,-0.69,-1],
    [0.03,0.93,-1],
    [0.12,0.25,-1],
    [0.96,0.47,-1],
    [0.80,-0.75,-1],
    [0.46,0.98,-1],
    [0.66,0.24,-1],
    [0.72,-0.15,-1],
    [0.35,0.01,-1],
    [-0.11,0.1,1],
    [0.31,-0.96,1],
    [0.0,-0.26,1],
    [-0.43,-0.65,1],
    [0.57,-0.97,1],
    [-0.72,-0.64,1],
    [-0.25,-0.43,1],
    [-0.12,-0.9,1],
    [-0.58,0.62,1],
    [-0.77,-0.76,1]
]

#Output
y = 0

#Best Fit
BEST_X = 0.77
BEST_Y = -0.55


## Step 1 - Initilization of variables

#Weights
weight = [0,0]

#Bias
bias = 1

#Threshold/Step Function
threshold = 0

#Learning Rate
learning_rate = 1

#Max Iterations
max_iterations = 10


## Step 2 - Loop and compute
for iteration in range(1, max_iterations):
    hits = 0
    print("\n---------------------Iteration Number " +str(iteration)+" ------------")

    #Send all data points into the computation
    for i in range(0,len(x)):
        sum = 0

        #weighted_sum, -1 since last index is the label
        for j in range(0,len(x[i])-1):
            sum += x[i][j] * weight[j]

        #Output = Bias + Weighted_sum
        output = bias + sum

        #Apply Activation on Output
        #Activation Function = {Value>0? 1: -1}
        print("---> Data Point Index (Before Wgt Update):", i,
             " Input:", x[i],
             " Weights:", weight,
             " Output Sum:", output)

        if output > threshold:
            y = 1
        else:
            y = -1

        #if output does not match with desired output, then update
        if y == x[i][2]:
            hits += 1
            answer = "" #"No Weight Change."
        else:
            for j in range(0,len(weight)):
                weight[j] = weight[j] + (learning_rate * x[i][2] * x[i][j])
            bias = bias + learning_rate * x[i][2]
            answer = "Weight Update has happened, New Weight is: "+str(weight)

        print("\n"+answer)

    if hits == len(x):
        print("\n--------------------------------------------")
        print("\nAlgorithm has learned with "+str(iteration)+" iterations!")
        break;
print("\nDone!\n")