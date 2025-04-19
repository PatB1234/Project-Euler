data = open("67_file.txt", "r").read()

# Parse the tree into an 2D array
tringle = [[int(word) for word in row.split()] for row in data.strip().split("\n")] # Writing this made me feel very smart :)
print(tringle)
#Bottom-Up Approach
for row_iter in reversed(range(len(tringle) - 1)):

    row = tringle[row_iter]
    for col_iter in range(len(row)):
        
        row[col_iter] += max(tringle[row_iter + 1][col_iter], tringle[row_iter + 1][col_iter + 1])

print(tringle[0][0])