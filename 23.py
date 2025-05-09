import math
import numpy as np

def isAbundant(n):

    factors = []
    for i in range(1, n):

        if(n != i and n % i == 0):

            factors.append(i)

    s = sum(factors)
    if s > n:

        return True
    else:

        return False
    

abundants = []
for i in range (1, 28124):

    if (isAbundant(i)):

        abundants.append(i)

vector = np.array(abundants)
matrix = np.broadcast_to(vector, (len(abundants), len(abundants))) # Get all possible sums
sums = matrix + matrix.T

areAbundants = np.ones((28125,)) # Returns an array filled with ones
notAundants = np.array([s for s in set(sums.flatten()) if s < 28125])
areAbundants[notAundants] = 0
print(sum(np.arange(len(areAbundants))[areAbundants == 1].tolist()))