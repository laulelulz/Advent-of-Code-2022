import copy

# Read input-file into list of lines

INPUT_FILE = "Day 5\input.txt"

with open(INPUT_FILE, 'r') as file:

    input_list = file.read().splitlines()


# split input_list into 2 lists: stack and moves

stacks = []
moves = []

for line in input_list:

    if line.startswith('move'):

        moves.append(line)
    
    elif line != '':

        stacks.append(line)


# sort stacks by stack instead of lines, so that each list entry is a stack and the sublist entries are sorted from bottom to top

number_of_stacks = int(stacks[-1][-2])
height_of_highest_stack = int(len(stacks)-1)
stacks_sorted = []
x = 1

for i in range(number_of_stacks):

    stacks_sorted.append([])

    for j in range(height_of_highest_stack):

        if stacks[j][3*i + x] != ' ':

            stacks_sorted[i].append(stacks[j][3*i + x])
    
    x += 1

for i in range(number_of_stacks):

    stacks_sorted[i] = list(reversed(stacks_sorted[i]))


# define function for moving items from one stack to another (part 1)

def move_item(stack_list: list, number_of_crates: int, stack_origin: int, stack_destination: int):

    for i in range(number_of_crates):

        stack_list[stack_destination-1].append(stack_list[stack_origin-1].pop())
    
    return stack_list


# define function for moving multiple items from one stack to another at once (part 2)

def move_item2(stack_list: list, number_of_crates: int, stack_origin: int, stack_destination: int):

    for i in range(number_of_crates):

        stack_list[stack_destination-1].append(stack_list[stack_origin-1].pop(i-number_of_crates))

    return stack_list


# feed intructions to move_item function

stacks_new1 = copy.deepcopy(stacks_sorted)
stacks_new2 = copy.deepcopy(stacks_sorted)

for line in moves:

    input_parameters = []

    for word in line.split(' '):

        if word.isdigit():

            input_parameters.append(int(word))
    
    final_stack1 = move_item(stacks_new1, input_parameters[0], input_parameters[1], input_parameters[2])
    final_stack2 = move_item2(stacks_new2, input_parameters[0], input_parameters[1], input_parameters[2])


# Create answer string (top crate of each stack)

answer_string1 = ''
answer_string2 = ''

for stack in final_stack1:

    answer_string1 += stack[-1]

for stack in final_stack2:

    answer_string2 += stack[-1]

print(answer_string1)
print(answer_string2)