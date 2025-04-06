fib = [0, 1]
sum = 0

while fib[-1] < 4000000:

    res = fib[len(fib)-2] + fib[len(fib)-1]
    print(fib)
    if res % 2 == 0:

        sum += res
    fib.append(res)

print(sum)

print("hi guys")
print("")