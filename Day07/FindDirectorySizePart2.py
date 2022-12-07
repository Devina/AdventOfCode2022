from collections import defaultdict

with open('ResultingTerminalOutput.txt', 'r') as f:
    content = f.readlines()

# Define variables
current_directory = ['outermost']
all_files_size_total = defaultdict(lambda: 0)
total_size = 0
remove = []

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
            
unused_space = 70000000 - all_files_size_total['outermost']  
space_to_free = 30000000 - unused_space
    
# Count size to remove
for key, value in all_files_size_total.items():
    if value >= space_to_free and value < all_files_size_total['outermost']:
        remove.append(value)
      
print("Total size of that directory to remove for update: ", min(remove))