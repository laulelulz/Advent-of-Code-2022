# load input file

with open("Day 6\input.txt", "r") as file:

    input_string = file.read()

# define function that checks after which index the input string has specified number of distinct characters

def check_marker(input_str: str, number_of_distinct_characters: int):

    for i in range(len(input_str)-number_of_distinct_characters+1):

        repetition = False

        for j in range(i, i + number_of_distinct_characters):

            if input_str[j] in (input_str[i:j] or input_str[(j+1):(i + number_of_distinct_characters)]):

                repetition = True
        
        if not repetition:

            return i + number_of_distinct_characters
    
    return -1

# use the thing

print(check_marker(input_string, 4))
print(check_marker(input_string, 14))