with open('CrateMoves.txt', 'r') as f:
    content = f.readlines()

# Define variables
one = ['Q','W','P','S','Z','R','H','D'] # Bottom crate in 0th element, and top crate on last element
two = ['V','B','R','W','Q','H','F']
three = ['C','V','S','H']  
four = ['H','F','G']
five = ['P','G','J','B','Z']
six = ['Q','T','J','H','W','F','L']
seven = ['Z','T','W','D','L','V','J','N']
eight = ['D','T','Z','C','J','G','H','F']
nine = ['W','P','V','M','B','H']
top_crates = []

# Loop through each items in the file
for line in content:
    line = line.split(',')
    crate_stack_to_move = (locals()[line[1].rstrip("\n")])[(int(line[0])*-1):]  # Take quantity to move and add to list
    for i in crate_stack_to_move:   # Iterate through crates to move and add to new stack
        (locals()[line[2].rstrip("\n")]).append(i)
    for crate in range(int(line[0])):   # Remove the moved crate from original stack
        (locals()[line[1].rstrip("\n")]).pop()

# Take top crate from each stack - This is the last element in each list
top_crates.append(one[-1])
top_crates.append(two[-1])
top_crates.append(three[-1])
top_crates.append(four[-1])
top_crates.append(five[-1])
top_crates.append(six[-1])
top_crates.append(seven[-1])
top_crates.append(eight[-1])
top_crates.append(nine[-1])

print("Crate on top of each stack after reassignment: ", ''.join(top_crates))
