with open('TreeGrid.txt', 'r') as f:
    content = f.readlines()

# Define variables
trees_in_coordinates = []
count = 1
all_distance = []

# Loop through each line in the file
for line in content:
    line = list(line.rstrip("\n"))
    trees_in_coordinates.append(list(line))

total_tree_one_direction = len(trees_in_coordinates)

all_distance = [[0 for x in range(total_tree_one_direction)] for y in range(total_tree_one_direction)]
for i in range(1, total_tree_one_direction - 1):
    for j in range(1, total_tree_one_direction - 1):
        
        # Column check - Top
        multiplier = 0
        for column in range(i-1, -1, -1):
            multiplier += 1
            if trees_in_coordinates[i][j] <= trees_in_coordinates[column][j]: 
                break
        
        all_distance[i][j] = multiplier
        
        # Column check - Bottom
        multiplier = 0
        for column in range(i+1, total_tree_one_direction):
            multiplier += 1
            if trees_in_coordinates[i][j] <= trees_in_coordinates[column][j]: 
                break
                        
        all_distance[i][j] *= multiplier
        
        # Row check - Right
        multiplier = 0
        for row in range(j+1, total_tree_one_direction):
            multiplier += 1
            if trees_in_coordinates[i][j] <= trees_in_coordinates[i][row]: 
                break
        
        all_distance[i][j] *= multiplier
        
        # Row check - Left
        multiplier = 0
        for row in range(j-1, -1, -1):
            multiplier += 1
            if trees_in_coordinates[i][j] <= trees_in_coordinates[i][row]: 
                break
                
        all_distance[i][j] *= multiplier


print("Highest scenic score possible for any tree: ", max(sum(all_distance, [])))