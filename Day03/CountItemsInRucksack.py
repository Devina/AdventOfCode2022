with open('RucksackItems.txt', 'r') as f:
    content = f.readlines()

# Define variables
items_in_both_compartments = []
item_priority_count = 0

# Loop through each items in the file
for line in content:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]    # Split in half and store in two variables
    for c in firstpart:
        if c in secondpart:
            items_in_both_compartments.append(c)
            secondpart = secondpart.replace(secondpart, '*', 1) # Replace the character with '*' if accounted for to ensure it does not account for that character multiple times
        
# Loop through items in both compartments extracted and calculate priority
for item in items_in_both_compartments:
    if item.isupper():
        item_priority_count += (ord(item) - 38) # Convert to Ascii and then minus 38 to get priority in range 27-52
    else:
        item_priority_count += (ord(item) - 96) # Convert to Ascii and then minus 96 to get priority in range 1-26
 
print("Sum of priorities of the items in both compartments: ", item_priority_count)