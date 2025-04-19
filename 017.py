base_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
tenPrefixes = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]

def count_letters(word):

    arr = list(word)
    count = 0
    for a in arr:

        if a != " ":
            count += 1

    return count

total_count = 0
for i in range(1, 1001):
    num_arr = [int(j) for j in list(str(i))]
    num_str = ""

    if i < 20:

        num_str = base_nums[i-1]
    elif i % 1000 == 0:

        num_str = base_nums[num_arr[0] - 1]  + " thousand"

    elif i % 100 == 0:

        num_str = base_nums[num_arr[0] - 1]  + " hundred"
    elif i % 10 == 0 and i > 100:

        num_str = base_nums[num_arr[0] - 1] + " hundred" + " and " + tenPrefixes[num_arr[1] - 1]
    elif i % 10 == 0 and i < 100:

        num_str = tenPrefixes[num_arr[0] - 1]
    elif i < 100:

        num_str = tenPrefixes[num_arr[0] - 1] + " " + base_nums[num_arr[1] - 1]

    elif i > 100 and i < 1000 and ( i - (num_arr[0] * 100)) > 10 and ( i - (num_arr[0] * 100)) < 20:
        
        num_str = base_nums[num_arr[0] - 1] + " hundred" + " and " + base_nums[num_arr[2] + 9]

    elif i > 100 and i < 1000 and num_arr[1] == 0:
        num_str = base_nums[num_arr[0] - 1] + " hundred" + " and " + base_nums[num_arr[2] - 1]

    elif i > 100 and i < 1000:
        num_str = base_nums[num_arr[0] - 1] + " hundred" + " and " + tenPrefixes[num_arr[1] - 1] + " " + base_nums[num_arr[2] - 1]

    
    total_count += count_letters(num_str)
print(total_count)