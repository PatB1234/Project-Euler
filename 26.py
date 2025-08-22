max = 0
l = 1
for i in range(1, 1000):

    remainders_seen = []
    r = -1
    n = 1
    while r not in remainders_seen:
        if r != -1:
            remainders_seen.append(r)
        r = (n * 10) % i
        n = r

    if len(remainders_seen) > max:

        max = len(remainders_seen)
        l = i

print(l, max)
