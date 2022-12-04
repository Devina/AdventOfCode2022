from intspan import intspan

with open('SectionAssignments.txt', 'r') as f:
    content = f.readlines()

# Define variables
first_range = []
second_range = []
overlap_count_total = 0

# Loop through each items in the file
for line in content:
    ranges = line.split(",")
    first_range = (ranges[0].split("-"))
    first_range = range(int(first_range[0]), (int(first_range[1])+1))
    second_range = (ranges[1].split("-"))
    second_range = range(int(second_range[0]), (int(second_range[1])+1))
    for n in first_range:
        if n in second_range:
            overlap_count_total += 1
            break   # Only want distinct count where it overlaps once, so once overlap is found, the loop can break
        
print("Assignment pairs where the ranges overlap: ", overlap_count_total)