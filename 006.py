squaredSum = 0
sumSquared = 0
for i in range (1, 101):
    squaredSum += i**2
    sumSquared += i

sumSquared = sumSquared ** 2

print(sumSquared-squaredSum)

