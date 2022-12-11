from math import lcm

with open('Notes.txt', 'r') as f:
    content = f.readlines()


# Define variables
monkey_0 = [97, 81, 57, 57, 91, 61]
monkey_1 = [88, 62, 68, 90]
monkey_2 = [74, 87]
monkey_3 = [53, 81, 60, 87, 90, 99, 75]
monkey_4 = [57]
monkey_5 = [54, 84, 91, 55, 59, 72, 75, 70]
monkey_6 = [95, 79, 79, 68, 78]
monkey_7 = [61, 97, 67]
inspection_count = [0, 0, 0, 0, 0, 0, 0, 0]
least_common_multiple = lcm(11, 19, 5, 2, 13, 7, 3, 17)


# Monkey actions
def monkey_0_reaction(worry_level):
    operation = worry_level * 7
    operation = operation % least_common_multiple
    if operation % 11 == 0:
        monkey_5.append(operation)
        monkey_0.pop(0)
        inspection_count[0] += 1
    else:
        monkey_6.append(operation)
        monkey_0.pop(0)
        inspection_count[0] += 1

def monkey_1_reaction(worry_level):
    operation = worry_level * 17
    operation = operation % least_common_multiple
    if operation % 19 == 0:
        monkey_4.append(operation)
        monkey_1.pop(0)
        inspection_count[1] += 1
    else:
        monkey_2.append(operation)
        monkey_1.pop(0)
        inspection_count[1] += 1

def monkey_2_reaction(worry_level):
    operation = worry_level + 2
    operation = operation % least_common_multiple
    if operation % 5 == 0:
        monkey_7.append(operation)
        monkey_2.pop(0)
        inspection_count[2] += 1
    else:
        monkey_4.append(operation)
        monkey_2.pop(0)
        inspection_count[2] += 1

def monkey_3_reaction(worry_level):
    operation = worry_level + 1
    operation = operation % least_common_multiple
    if operation % 2 == 0:
        monkey_2.append(operation)
        monkey_3.pop(0)
        inspection_count[3] += 1
    else:
        monkey_1.append(operation)
        monkey_3.pop(0)
        inspection_count[3] += 1

def monkey_4_reaction(worry_level):
    operation = worry_level + 6
    operation = operation % least_common_multiple
    if operation % 13 == 0:
        monkey_7.append(operation)
        monkey_4.pop(0)
        inspection_count[4] += 1
    else:
        monkey_0.append(operation)
        monkey_4.pop(0)
        inspection_count[4] += 1

def monkey_5_reaction(worry_level):
    operation = worry_level * worry_level
    operation = operation % least_common_multiple
    if operation % 7 == 0:
        monkey_6.append(operation)
        monkey_5.pop(0)
        inspection_count[5] += 1
    else:
        monkey_3.append(operation)
        monkey_5.pop(0)
        inspection_count[5] += 1

def monkey_6_reaction(worry_level):
    operation = worry_level + 3
    operation = operation % least_common_multiple
    if operation % 3 == 0:
        monkey_1.append(operation)
        monkey_6.pop(0)
        inspection_count[6] += 1
    else:
        monkey_3.append(operation)
        monkey_6.pop(0)
        inspection_count[6] += 1

def monkey_7_reaction(worry_level):
    operation = worry_level + 4
    operation = operation % least_common_multiple
    if operation % 17 == 0:
        monkey_0.append(operation)
        monkey_7.pop(0)
        inspection_count[7] += 1
    else:
        monkey_5.append(operation)
        monkey_7.pop(0)
        inspection_count[7] += 1


# Loop through 10000 rounds and run through inspections
for i in range(10000):
    if len(monkey_0) > 0:
        for j in range(len(monkey_0)):
            monkey_0_reaction(monkey_0[0])
    if len(monkey_1) > 0:
        for j in range(len(monkey_1)):
            monkey_1_reaction(monkey_1[0])
    if len(monkey_2) > 0:
        for j in range(len(monkey_2)):
            monkey_2_reaction(monkey_2[0])
    if len(monkey_3) > 0:
        for j in range(len(monkey_3)):
            monkey_3_reaction(monkey_3[0])
    if len(monkey_4) > 0:
        for j in range(len(monkey_4)):
            monkey_4_reaction(monkey_4[0])
    if len(monkey_5) > 0:
        for j in range(len(monkey_5)):
            monkey_5_reaction(monkey_5[0])
    if len(monkey_6) > 0:
        for j in range(len(monkey_6)):
            monkey_6_reaction(monkey_6[0])
    if len(monkey_7) > 0:
        for j in range(len(monkey_7)):
            monkey_7_reaction(monkey_7[0])


print("The level of monkey business after 10000 rounds: ", sorted(inspection_count)[-1]*sorted(inspection_count)[-2])
