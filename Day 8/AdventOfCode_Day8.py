# Import file and put in list of single lines. Split up single lines into sublists of digits.
FILENAME = "Day 8\input.txt"

with open(FILENAME, "r") as file:

    lines_temp = file.read().splitlines()
    lines = []

    for i in range(len(lines_temp)):

        lines.append([])

        for j in range(len(lines_temp[i])):

            lines[i].append(int(lines_temp[i][j]))

# Define function that finds visible trees from one side. This function can be reused for all directions, we just have to pivot the list accordingly.
# Each tree gets an unique identifier in the form [column, row] to avoid trees being counted twice.

def find_visible_trees(input_list: list):

    visible_trees = []

    for i in range(len(input_list)):

        highest_tree = -1

        for j in range(len(input_list[i])):

            if input_list[i][j] > highest_tree:

                highest_tree = input_list[i][j]
                visible_trees.append([i, j])
    
    return visible_trees


# Make function to reverse each sublist of lines, so lines[i][j] -> lines[i][-(j+1)]

def reverse_lines(input_list: list):

    reversed_lines = []

    for i in range(len(input_list)):

        reversed_lines.append([])

        for j in range(len(input_list[i])):

            reversed_lines[i].append(input_list[i][-(j+1)])

    return reversed_lines


# Indices in reversed list are counted from the wrong side. To make them the same as the indices as in the original list, we need to transform them.
# To do that, we find out how many sublists each list entry contains (number of sublists = x), then transform 0 -> x-1, 1 -> x-2, and so forth.

def transform_indices_row(input_list_for_length: list, input_list_to_transform: list):

    x = len(input_list_for_length[0])
    transformed_list = []

    for i in range(len(input_list_to_transform)):

        transformed_list.append([])
        transformed_list[i].append(input_list_to_transform[i][0])
        transformed_list[i].append(x-input_list_to_transform[i][1]-1)

    return transformed_list


# For pivoted lists, we need a similar function:

def transform_indices_column(input_list_for_length: list, input_list_to_transform: list):

    x = len(input_list_for_length)
    transformed_list = []

    for i in range(len(input_list_to_transform)):

        transformed_list.append([])
        transformed_list[i].append(input_list_to_transform[i][1])
        transformed_list[i].append(input_list_to_transform[i][0])

    return transformed_list


# To count the visible trees from top and bottom, we need another function to pivot our input list, so rows -> columns and columns -> rows.

def pivot_list(input_list: list):

    pivot_list = []

    for j in range(len(input_list[0])):

        pivot_list.append([])

    for i in range(len(input_list)):

        for j in range(len(input_list[i])):

            pivot_list[j].append(input_list[i][j])

    return pivot_list


# Make list of all trees visible from the left.

left_visible_trees = find_visible_trees(lines)

# Make list of all trees visible from the right.

right_visible_trees_temp = find_visible_trees(reverse_lines(lines))
right_visible_trees = transform_indices_row(lines, right_visible_trees_temp)

# Make list of all trees visible from the top.

top_visible_trees_temp = find_visible_trees(pivot_list(lines))
top_visible_trees = transform_indices_column(lines, top_visible_trees_temp)

# Make list of all trees visible from the bottom.

bottom_visible_trees_temp = find_visible_trees(reverse_lines(pivot_list(lines)))
bottom_visible_trees = transform_indices_column(lines, transform_indices_row(lines, bottom_visible_trees_temp))


# Now that we have transformed all visible trees into the same unique tree identifiers, we add them into one list, while leaving out duplicates

def add_if_not_included(list_to_add_to: list, list_to_add_from: list):

    for element in list_to_add_from:

        if element not in list_to_add_to:

            list_to_add_to.append(element)
    
    return list_to_add_to

all_visible_trees = []
all_visible_trees = add_if_not_included(all_visible_trees, left_visible_trees)
all_visible_trees = add_if_not_included(all_visible_trees, right_visible_trees)
all_visible_trees = add_if_not_included(all_visible_trees, top_visible_trees)
all_visible_trees = add_if_not_included(all_visible_trees, bottom_visible_trees)


# Check number of total visible trees

print (len(all_visible_trees))