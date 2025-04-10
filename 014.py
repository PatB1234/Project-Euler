def get_sequence_length(start_num):

    list = [start_num]
    curr_no = start_num
    while list[-1] != 1:
        if (curr_no % 2 == 0): # is the number even

            curr_no = curr_no/2
        else: #is the number odd

            curr_no = curr_no * 3 + 1
        
        list.append(curr_no)

    return len(list)


curr_largest_start = 13
curr_largest_chain = 10
for i in range (13, 1000000):

    sequence_length = get_sequence_length(i)
    if sequence_length > curr_largest_chain:

        curr_largest_chain = sequence_length
        curr_largest_start = i
    
print(curr_largest_start)