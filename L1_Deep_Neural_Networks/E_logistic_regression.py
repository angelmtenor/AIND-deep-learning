import numpy as np

# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


def prediction(X, W, b):
    return sigmoid(np.matmul(X, W) + b)


def error_vector(y, y_hat):
    return [-y[i] * np.log(y_hat[i]) - (1 - y[i]) * np.log(1 - y_hat[i]) for i in range(len(y))]


def error(y, y_hat):
    ev = error_vector(y, y_hat)
    return sum(ev) / len(ev)


# EXERCISE: Fill in the code below to calculate the gradient of the error function.
# The result should be a list of three lists:
# The first list should contain the gradient (partial derivatives) with respect to w1
# The second list should contain the gradient (partial derivatives) with respect to w2
# The third list should contain the gradient (partial derivatives) with respect to b
def dErrors(X, y, y_hat):
    y_hat = np.reshape(y_hat, -1)
    DErrorsDx1 = (y-y_hat) * X[:, 0]
    DErrorsDx2 = (y-y_hat) * X[:, 1]
    DErrorsDb = y-y_hat
    return DErrorsDx1, DErrorsDx2, DErrorsDb


# EXERCISE: Fill in the code below to implement the gradient descent step.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b.
# It should calculate the prediction, the gradients, and use them to
# update the weights and bias W, b. Then return W and b.
# The error e will be calculated and returned for you, for plotting purposes.
def gradientDescentStep(X, y, W, b, learn_rate=0.01):
    # EXERCISE: Calculate the prediction
    y_hat = prediction(X, W, b)
    # EXERCISE: Calculate the gradient
    gradient = dErrors(X, y, y_hat)
    # EXERCISE: Update the weights  W -= learn_rate *
    W[0] += learn_rate * np.sum(gradient[0])
    W[1] += learn_rate * np.sum(gradient[1])
    b += learn_rate * np.sum(gradient[2])
    # This calculates the error
    e = error(y, y_hat)
    return W, b, e


# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainLR(X, y, learn_rate=0.01, num_epochs=100):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    # Initialize the weights randomly
    W = np.array(np.random.rand(2, 1)) * 2 - 1
    b = np.random.rand(1)[0] * 2 - 1
    # These are the solution lines that get plotted below.
    boundary_lines = []
    errors = []
    for i in range(num_epochs):
        # In each epoch, we apply the gradient descent step.
        W, b, error = gradientDescentStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0] / W[1], -b / W[1]))
        errors.append(error)
    return boundary_lines, errors


data = np.genfromtxt('B_data.csv', delimiter=',')
trainLR((data[:, 0:2]), data[:, 2])
