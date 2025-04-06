arr = []
maxPrime = 2000000
primeBoolArr = [True] * (maxPrime)
currPrime = 2
while (currPrime ** 2 <= maxPrime):

    if (primeBoolArr[currPrime]): # Checking if the current iterator is a prime

        for i in range(currPrime ** 2, maxPrime, currPrime):

            primeBoolArr[i] = False # Set all mutiples of our prime to False i.e. they are not primes

    currPrime += 1
    
# Add all the prime numbers to an array
for i in range (2, maxPrime): 
    
    if (primeBoolArr[i] and i != 1): # 1 is not a prime so we don't even consider it   

        arr.append(i)

print(sum(arr))
