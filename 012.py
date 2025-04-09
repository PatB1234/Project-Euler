import math

def get_num_factors(num):
    factors = []
    for i in range (1, int(math.sqrt(num)) + 1): # Factors come in pairs

        if num % i == 0:

            factors.append(i)
            if i != num // i:

                factors.append(i)

    return(len(factors))

def get_triangle_numbers(tringle_no):

    sum = 0

    for i in range (0, tringle_no):
        sum += i + 1

    return sum


i = 1
while (get_num_factors(get_triangle_numbers(i)) < 500):

    i += 1

print(get_triangle_numbers(i)) # Return the triangle number

