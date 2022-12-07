from collections import defaultdict

with open('ResultingTerminalOutput.txt', 'r') as f:
    content = f.readlines()

# Define variables
current_directory = ['outermost']
all_files_size_total = defaultdict(lambda: 0)
total_size = 0

# Loop through each line in the file
for line in content:
    line = line.strip().split()
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                current_directory.pop()
            elif line[2] == "/":
                current_directory = ['outermost']
            else:
                current_directory.append(line[2])
    elif line[0] != "dir":
        cd_str = ''
        for dir in current_directory:
            cd_str += dir
            all_files_size_total[cd_str] += int(line[0])
    
# Count size
for key, value in all_files_size_total.items():
    if value <= 100000:
        total_size += value
    
print("Sum of the total sizes of those directories (Where less than total size of 1000): ", total_size)