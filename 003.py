import math
n = 600851475143
nums = []
while n % 2 == 0:

    n = n // 2
    nums.append(2)


for i in range (3, int(math.sqrt(n))):
    while n % i == 0:
        n = n // i 
        nums.append(i)

print(nums)