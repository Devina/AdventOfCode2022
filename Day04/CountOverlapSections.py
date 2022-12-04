with open('SectionAssignments.txt', 'r') as f:
    content = f.readlines()

# Define variables
first_range = []
second_range = []
overlap_count = 0   # Counter for section assignment overlap (Per pair)
range_contain_other = 0 # Counter for occurance where session assignment fully contains the other

# Loop through each items in the file
for line in content:
    ranges = line.split(",")
    first_range = (ranges[0].split("-"))
    first_range = range(int(first_range[0]), (int(first_range[1])+1))
    second_range = (ranges[1].split("-"))
    second_range = range(int(second_range[0]), (int(second_range[1])+1))
    for n in first_range:
        if n in second_range:
            overlap_count += 1
    if min(len(first_range), len(second_range)) == overlap_count:   # If fully contained session assignment, then the count for the lower range should match the overlap count
        range_contain_other += 1
    overlap_count = 0   # Reset counter for next pair
        
print("Assignment pairs where one range fully contain the other: ", range_contain_other)
