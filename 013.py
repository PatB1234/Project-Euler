# The file given has each number
sum = 0

with open("013_file.txt", "r") as numFile:

    for i in numFile.readlines():

        sum += int(i)

    numFile.close()

print(str(sum)[0:10])