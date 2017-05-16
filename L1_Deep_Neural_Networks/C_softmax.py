import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    return np.exp(L) / np.sum(np.exp(L))

res = softmax([1, 8, 16])
print(res, '\nsum =', sum(res))