curr_largest = 0

for i in range (100, 999):

    for j in range (100, 999):

        num =  i * j
        
        numBack = (int(str(num)[::-1]))
        if (num == numBack and num > curr_largest):

            curr_largest = num

print(curr_largest)