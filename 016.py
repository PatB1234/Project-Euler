# Pretty simple, splitting the string was the hardest part tbh
import math

num = str(int(math.pow(2, 1000)))
numArr = []
for n in num:

    numArr.append(int(n))


print(sum(numArr))