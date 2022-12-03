with open('RucksackItems.txt', 'r') as f:
    content = f.readlines()

# Define variables
group_items = []
elf_badges = []
badges_priority_count = 0

# Loop through each items in the file
for line in content:
    group_items.append(line.rstrip("\n"))   # Obtain group and remove new line from the items
    if len(group_items) == 3:
        group_badge = set.intersection(*map(set,group_items)) # Get common characters at any position by using a set intersection over all strings
        for value in group_badge: # To get value in set as a string
            elf_badges.append(value)
        group_items = []    # Reset the group
        
# Loop through badges and calculate priority
for badge in elf_badges:
    if badge.isupper():
        badges_priority_count += (ord(badge) - 38)
    else:
        badges_priority_count += (ord(badge) - 96)
 
print("Sum of priorities of the badges: ", badges_priority_count)