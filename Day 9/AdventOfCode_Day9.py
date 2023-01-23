# Import input file and parse lines into a list with the instructions as sublists.

FILENAME = 'Day 9\input.txt'

with open(FILENAME, 'r') as file:

    instructions_temp = file.read().splitlines()
    instructions = []

    for line in instructions_temp:

        instructions.append(line.split(' '))


# Build up grid with nested list.

grid = [['o']]

# Head-Moves either go to an existing spot in the grid or create a new spot. New spots are marked 'o'.

def head_move(direction: str, current_row: int, current_column: int):

    global grid
    global knot_positions

    if direction == 'R':

        if current_column + 2 > len(grid[current_row]):

            for i in range(len(grid)):

                grid[i].append('o')
        
        new_row = current_row
        new_column = current_column + 1

    elif direction == 'L':

        if current_column == 0:

            grid_temp = []

            for i in range(len(grid)):

                grid_temp.append([])
                grid_temp[i].append('o')

                for j in range(len(grid[i])):

                    grid_temp[i].append(grid[i][j])
            
            grid = grid_temp        
            new_row = current_row
            new_column = current_column

            for i in range(1,10):

                knot_positions[i][1] += 1
        
        else:

            new_row = current_row
            new_column = current_column - 1

    elif direction == 'D':

        if current_row + 2 > len(grid):

            grid.append([])

            for i in range(len(grid[current_row])):

                grid[current_row + 1].append('o')
            
        new_row = current_row + 1
        new_column = current_column

    elif direction == 'U':

        if current_row == 0:

            grid_temp = [[]]

            for i in range(len(grid[0])):

                grid_temp[0].append('o')

            for i in range (1, len(grid)+1):

                grid_temp.append([])

                for j in range (len(grid[0])):

                    grid_temp[i].append(grid[i-1][j])

            grid = grid_temp
            new_row = current_row
            new_column = current_column

            for i in range (1,10):

                knot_positions[i][0] += 1
        
        else:

            new_row = current_row - 1
            new_column = current_column

    return [new_row, new_column]







# Check if Tail moves and if so, where to.

def tail_move(head_row: int, head_column: int, current_row: int, current_column: int):

    if head_row == current_row:

        new_row = current_row

        if head_column > current_column +1:

            new_column = current_column + 1

        elif head_column < current_column -1:

            new_column = current_column -1

        else:

            new_column = current_column
    
    if head_row == current_row +1 or head_row == current_row -1:

        if head_column in range (current_column -1, current_column +2):

            new_row = current_row
            new_column = current_column
        
        elif head_column > current_column +1:

            new_row = head_row
            new_column = current_column +1

        elif head_column < current_column -1:

            new_row = head_row
            new_column = current_column -1

    elif head_row > current_row +1:

        new_row = current_row +1
        
        if current_column > head_column:

            new_column = current_column -1
        
        elif current_column < head_column:

            new_column = current_column +1
        
        else:

            new_column = head_column

    elif head_row < current_row -1:

        new_row = current_row -1
        
        if current_column > head_column:

            new_column = current_column -1
        
        elif current_column < head_column:

            new_column = current_column +1
        
        else:

            new_column = head_column


    return [new_row, new_column]




# moves function: gets input from instructions and calls the appropriate function. For example R 4 calls the function to move the head right and then the function to check if and where the Tail should move 4 times in a row.
# Each spot of the grid the Tail passes gets marked 'x'.


#head_position = [0,0]
#tail_position = [0,0]

#for line in instructions:

#    for i in range(int(line[1])):

#        head_position = head_move(line[0], head_position[0], head_position[1])
#        tail_position = tail_move(head_position[0], head_position[1], tail_position[0], tail_position[1])


#        if grid[tail_position[0]][tail_position[1]] == 'o':

#            grid[tail_position[0]][tail_position[1]] = 'x'






# ------------ Part 2 ------------

# Write know positions into list:

knot_positions = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]


for line in instructions:

    for i in range(int(line[1])):

        knot_positions[0] = head_move(line[0], knot_positions[0][0], knot_positions[0][1])
        
        for i in range(1,10):

            knot_positions[i] = tail_move(knot_positions[i-1][0], knot_positions[i-1][1], knot_positions[i][0], knot_positions[i][1])


        if grid[knot_positions[9][0]][knot_positions[9][1]] == 'o':

            grid[knot_positions[9][0]][knot_positions[9][1]] = 'x'



# Count all spots marked 'x'.

sum = 0

for i in range(len(grid)):

    for j in range(len(grid[i])):

        if grid[i][j] == 'x':
        
                    sum += 1

print (sum)
