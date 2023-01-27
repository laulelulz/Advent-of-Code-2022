FILENAME = "Day 11\input.txt"

with open(FILENAME, 'r') as file:

    input_str = file.read()

import math

class Monkey:

    def __init__(self, starting_items: list, operation: list, divisible_by: int, if_true: int, if_false: int, inspected_items: int):

        self.starting_items = starting_items
        self.operation = operation
        self.divisible_by = divisible_by
        self.if_true = if_true
        self.if_false = if_false
        self.inspected_items = inspected_items
    

    def execute_operation(self, operation, starting_items):

        temp_list = []

        for item in starting_items:

            if operation[1] == 'old':

                second_number = item
            
            else:

                second_number = operation[1]

            if operation[0] == '+':

                temp_list.append(int(item) + int(second_number))
            
            elif operation[0] == '*':

                temp_list.append(int(item) * int(second_number))
        
        return temp_list

    def single_monkey_turn (self, monkey_id, items_after_operation: list, divisible_by_temp: int, if_true_temp: int, if_false_temp: int):

        global monkeys

        for i in range(len(items_after_operation)):

            monkey_id.inspected_items += 1

            if items_after_operation[0] % divisible_by_temp == 0:

                monkeys[if_true_temp].starting_items.append(items_after_operation.pop(0))
            
            else:

                monkeys[if_false_temp].starting_items.append(items_after_operation.pop(0))
        
        monkey_id.starting_items = []

    def __str__(self):

        return (f"""Starting items: {self.starting_items}
Operation: new = old {self.operation[0]} {self.operation[1]}
Test: divisible by {self.divisible_by}
    If true: throw to monkey {self.if_true}
    If false: throw to monkey {self.if_false}""")


### Parse inputs into easy-to-read nested list

def parse_input_list(input_string):

    input_list_temp1 = input_string.split('\n\n')
    input_list_temp2 = []
    final_list = []

    for i in range(len(input_list_temp1)):

        input_list_temp2.append(input_list_temp1[i].split('\n'))
        final_list.append([])

        for j in range(len(input_list_temp2[i])):

            split = input_list_temp2[i][j].split(':')
            final_list[i].append([])

            for x in split:

                split2 = x.split(' ')

                for y in split2:

                    if y == '':

                        pass

                    elif y.endswith(','):

                        final_list[i][j].append(y[:len(y)-1])
                        pass

                    else:
                        final_list[i][j].append(y)

    for i in range (len(final_list)):

        for j in range(2):

            final_list[i][1].pop(0)

        for j in range(4):

            final_list[i][2].pop(0)
        
        for j in range(3):

            final_list[i][3].pop(0)
        

    return final_list


def one_round():

    for i in range(len(monkeys)):

        items_after_operation = monkeys[i].execute_operation(monkeys[i].operation, monkeys[i].starting_items)

        monkeys[i].single_monkey_turn(monkeys[i], items_after_operation, monkeys[i].divisible_by, monkeys[i].if_true, monkeys[i].if_false)


### Save monkeys in Monkey class

input_list = parse_input_list(input_str)

monkeys = []

for i in range(len(input_list)):

    monkeys.append(["Monkey " + str(i)])

    monkeys[i] = Monkey(input_list[i][1], input_list[i][2], int(input_list[i][3][0]), int(input_list[i][4][-1]), int(input_list[i][5][-1]), 0)



### Check 'monkey_business' (= multiplication of inspected_items of the two most active monkeys)

for i in range(10000):

    one_round()
    print (i)

inspected_list = []

for monkey in monkeys:

    inspected_list.append(monkey.inspected_items)

most_active_monkey = max(inspected_list)

inspected_list.sort()
inspected_list.pop()

second_most_active_monkey = max(inspected_list)

monkey_business = most_active_monkey * second_most_active_monkey

print (monkey_business)