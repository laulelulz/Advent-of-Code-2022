# get input string from file

FILENAME = "Day 7\input.txt"
with open(FILENAME, "r") as file:

    input_list = file.read().splitlines()


# build folder structure

def build_folder (command_prompt_lines: list):

    root = {}
    cd = root
    prev = []                                                       # cd as list

    for i in range(len(command_prompt_lines)):

        commands = command_prompt_lines[i].split(" ")

        if commands[0] == "$":

            if commands[1] == "cd":

                if commands[2] == "/":                              # sets current directory (cd) to root

                    cd = root

                elif commands[2] == "..":                           # removes last entry from prev

                    cd = prev.pop()

                elif len(commands) == 3:                            # sets current directory to the specified directory with name commands[2]

                    prev.append(cd)
                    cd = cd.get(commands[2])
                
            elif commands[1] == "ls":                               # lists contents of current directory. everything after this line is content of cd

                pass

        elif commands[0] == "dir":                                  # adds directory with the name commands[2] to current directory

            cd.update({commands[1]: {}})
        
        elif commands[0].isnumeric():

            cd.update({commands[1]: int(commands[0])})

    return root

# find total total_size of directory and write new directory with sizes of each sub-directory

def directory_size(directory: dict):

    total_size = 0
    global sub_dir_sizes

    for value in directory.values():

        if type(value) == type(int()):

            total_size += value
        
        elif type(value) == type(dict()):
            
            temp_size = directory_size(value)
            total_size += temp_size
            sub_dir_sizes.append(temp_size)
        
    return total_size

# write sizes of all directories into new dictionary

root = build_folder(input_list)
sub_dir_sizes = []
root_size = directory_size(root)

# ---PART 1---
# add up all sub directories with a file size up to 100 000

sum = 0

for i in sub_dir_sizes:

    if (i <= 100000):
        
        sum += i

print (sum)

# ---PART 2---
# find out which directory to delete - the smallest directory that leaves root with at least 30 000 000 unused space (total space of root is 70 000 000)

free_space_before_delete = 70000000 - root_size
space_to_free = 30000000 - free_space_before_delete

possible_directories = []

for i in sub_dir_sizes:

    if (i >= space_to_free):

        possible_directories.append(i)

print (min(possible_directories))