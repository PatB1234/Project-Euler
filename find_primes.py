def findPrimes(maxUpperBound):

    listOfPrimes = []
    marks = [False] * (maxUpperBound + 1)
    for i in range (2, maxUpperBound + 1):

        if marks[i] == False:

            listOfPrimes.append(i)
            for j in range (i ** 2, maxUpperBound + 1, i):
                marks[j] = True
    return listOfPrimes

