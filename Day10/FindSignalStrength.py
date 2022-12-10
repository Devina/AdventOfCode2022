with open('Instructions.txt', 'r') as f:
    content = f.readlines()


# Define variables
cycle_count = 1
register_X = 1
signal_strength = []


# Checks for cycle count at intervals
def cycle_count_check():
    if cycle_count == 20:
        signal_strength.append(20 * register_X)
    elif cycle_count == 60:
        signal_strength.append(60 * register_X)
    elif cycle_count == 100:
        signal_strength.append(100 * register_X)
    elif cycle_count == 140:
        signal_strength.append(140 * register_X)  
    elif cycle_count == 180:
        signal_strength.append(180 * register_X) 
    elif cycle_count == 220:
        signal_strength.append(220 * register_X)   


# Loop through each line in the file
for line in content:
    if 'noop' in line:
        cycle_count += 1
        cycle_count_check()
    elif 'addx ' in line:
        cycle_count += 1
        cycle_count_check()
        cycle_count += 1
        action, register_increment = line.split(" ")
        register_X += int(register_increment)
        cycle_count_check()
        

print("The sum of these six signal strengths: ", sum(signal_strength))