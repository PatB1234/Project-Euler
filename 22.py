names = [str(name) for name in open("22_file.txt", "r").readline().split(",")]
names.sort() # Sort each word name alphabetically
sum = 0

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range (1, len(names)+1):

    splitWord = list(names[i - 1]) # Convert each name to an array of its letters
    wordSum = 0
    for letter in splitWord:
        for j in range(len(letters)):

            if (letter == letters[j]):
                wordSum += j + 1
    
    sum += wordSum * i

print(sum)

