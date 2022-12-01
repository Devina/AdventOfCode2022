from collections import defaultdict

with open('ElfCalories.txt', 'r') as f:
    content = f.readlines()

# Define variables
elf_in_dictionary = {}
i = 0
calories_count = 0
top_three_elves_calories = 0

# Loop through each calories in the file and add to dictionary variable - Elf count starts at 0
for line in content:
    if line == '\n':    # If new line then move to next key in dictionary
        i+=1
        calories_count = 0
    else:
        calories_count += int(line)
        elf_in_dictionary[i] = calories_count
        

#print("Count of all elf calories (Elf number starting at 0): ", elf_in_dictionary)    # Debug: Print full dictionary
#print("Count of number of elves sharing calories: ", len(elf_in_dictionary)) # Debug: Count of number of elves
elf_with_max_calories = max(elf_in_dictionary, key=elf_in_dictionary.get)
#print("Elf number with max calories): ", elf_with_max_calories+1)   # Debug: Elf number - Add 1 as dictionary starts at 0 but that is elf number 1
print("Max calories being carried: ", elf_in_dictionary[elf_with_max_calories]) # Max calories the elf is carrying


# Sort the dictionary in descending order by value
sort_data = sorted(elf_in_dictionary.items(), key=lambda x: x[1], reverse=True)
#for i in sort_data:    # Debug: To see the full dictionary printed in descending order
#    print(i[0], i[1])  
for i in range(3):
    top_three_elves_calories += int(sort_data[i][1])
   
print("Top three elves calories added together: ", top_three_elves_calories) # Max calories the top three elves are carrying