with open("Day 4\input.txt", "r") as file:

    input_string = file.read()


input_list = input_string.splitlines()

# Split strings into sublists by character


def split_into_sublists(input: list, split_character: str):

    sublist = []

    for i in range(len(input)):

        sublist.append(input[i].split(split_character))

    return sublist

# Use split_into_sublists function twice to split input_list

sublist1 = split_into_sublists(input_list, ',')
sublist2 = []

for i in range(len(sublist1)):

    sublist2.append(split_into_sublists(sublist1[i], '-'))

# Convert strings to int in sublist2

for i in range(len(sublist2)):

    for j in range(len(sublist2[i])):

        for k in range(len(sublist2[i][j])):

            sublist2[i][j][k] = int(sublist2[i][j][k])


# Check if one pair fits into other

def check_pair(pair: list):


    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:

        return True

    elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:

        return True

    else:

        return False


# Count occurrences of one pair fitting into the other

sum = 0

for i in range(len(sublist2)):

    if check_pair(sublist2[i]):

        sum += 1

print (sum)


# Check if pairs overlap


def overlap(pair: list):

    for entry in range(pair[0][0], pair[0][1] + 1):

        if entry in range(pair[1][0], pair[1][1] + 1):

            return True
    
    return False


# Count occurrences of pairs that overlap


sum2 = 0

for i in range(len(sublist2)):

    if overlap(sublist2[i]):

        sum2 += 1

print (sum2)