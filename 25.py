fib = [1, 1]
num_dig = 1
while(num_dig != 1000):

    fib.append(fib[-1] + fib [-2])
    num_dig = len(str(fib[-1]))

print(len(fib))