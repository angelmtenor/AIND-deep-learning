import numpy as np


# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    Y, P = np.array(Y), np.array(P)  # (1-Y) operation cannot be performed on lists
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))


y = [1, 1, 0]
p = [0.8, 0.7, 0.1]
print(cross_entropy(y, p))
