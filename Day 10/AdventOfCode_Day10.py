FILENAME = "Day 10\input.txt"

with open(FILENAME, "r") as file:

    input_temp = file.read().splitlines()
    input_list = []
    
    for line in input_temp:

        input_list.append(line.split(" "))


# PART 1

def number_of_cycles(input_line: list):

    if input_line == ["noop"]:

        return 1
    
    if input_line[0] == "addx":

        return 2

def new_value(input_line: list, current_value: int):

    if input_line == ["noop"]:

        return current_value

    if input_line[0] == "addx":

        return current_value + int(input_line[1])



def signal_strength(cycle: int, value: int):

    return cycle*value



value_at_cycles = []
value = 1

for x in range(len(input_list)):

    cycles = number_of_cycles(input_list[x])
    

    for y in range(cycles):

        value_at_cycles.append(value)

    value = new_value(input_list[x], value_at_cycles[-1])



relevant_values = [20, 60, 100, 140, 180, 220]
sum = 0


for entry in relevant_values:

    sum += signal_strength(entry, value_at_cycles[entry -1])

print (sum)



# PART 2

display = ""

def lit_or_dark(cycle: int, position: int):

    if position == 0 and value_at_cycles[cycle-1] in range(0, 3):

        return "#"

    if position in range(value_at_cycles[cycle-1]-1, value_at_cycles[cycle-1]+2):

        return "#"

    return "."


for i in range(6):

    for j in range(40):

        display += lit_or_dark((i*40)+j+1, j)

    display += "\n"

print (display)