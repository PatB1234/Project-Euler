def d(n: int):

    factor_sum = 0
    for i in range(1, n):

        if n % i == 0 and n != i:

            factor_sum += i

    return factor_sum

list_num = []
for i in range(1, 10000):
    b = d(i)
    a = d(b)
    if (i == a) and (b != a):

        list_num.append(b)

print(sum(list_num) )

