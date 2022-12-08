with open('TreeGrid.txt', 'r') as f:
    content = f.readlines()

# Define variables
trees_in_coordinates = []
trees_visible = []
trees_visible_check = ['Yes', 'Yes', 'Yes', 'Yes'] # [Top, Right, Bottom, Left]


# Loop through each line in the file
for line in content:
    line = list(line.rstrip("\n"))
    trees_in_coordinates.append(list(line))

total_tree_one_direction = len(trees_in_coordinates)

for i in range(total_tree_one_direction): # i is row
    for j in range(total_tree_one_direction): # j is column
        if (i == 0) or (j == 0) or (i == total_tree_one_direction - 1) or (j == total_tree_one_direction - 1):
            trees_visible_check = ['Yes', 'Yes', 'Yes', 'Yes']
        
        # Column check
        for column in range(total_tree_one_direction):
            if column == i:
                pass
            else:
                if i >= column:
                    if trees_in_coordinates[i][j] <= trees_in_coordinates[column][j]:
                        trees_visible_check[3] = 'No'
                elif i <= column:
                    if trees_in_coordinates[i][j] <= trees_in_coordinates[column][j]:
                        trees_visible_check[1] = 'No'
        
        
        # Row check
        for row in range(total_tree_one_direction):
            if row == j:
                pass
            else:
                if j >= row:
                    if trees_in_coordinates[i][j] <= trees_in_coordinates[i][row]:
                        trees_visible_check[0] = 'No'
                elif j <= row:
                    if trees_in_coordinates[i][j] <= trees_in_coordinates[i][row]:
                        trees_visible_check[2] = 'No'
        
        if 'Yes' in trees_visible_check:
            trees_visible.append(trees_in_coordinates[i][j])
        
        trees_visible_check = ['Yes', 'Yes', 'Yes', 'Yes']   # Reset

    
print("Count of visible trees: ", len(trees_visible))