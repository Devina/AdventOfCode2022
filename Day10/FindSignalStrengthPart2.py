with open('Instructions.txt', 'r') as f:
    content = f.readlines()

# Define variables
current_crt_position = -1
register_X = 1
sprite_position = [0, 1, 2]
row_pixel = []
final_pic = []


# Set Pixel options; # or .
def pixel_choice():
    if current_crt_position in sprite_position:
        row_pixel.append('#')
    else:
        row_pixel.append('.')      
        
        
# Checks row and if it's size 40 then reset variables
def pixel_row_check():
    global row_pixel 
    global current_crt_position    
    if len(row_pixel) == 40:
        final_pic.append(row_pixel)
        row_pixel = []
        current_crt_position = -1  

        
# Loop through each line in the file
for line in content:
    
    if 'noop' in line:
        current_crt_position += 1
        pixel_choice()            
        pixel_row_check()      
    elif 'addx ' in line:
        current_crt_position += 1
        pixel_choice()
        pixel_row_check()
            
        current_crt_position += 1
        pixel_choice()
        pixel_row_check()
        
        action, register_increment = line.split(" ")
        register_X += int(register_increment)
        
        for i in range(len(sprite_position)):
            sprite_position[i] += int(register_increment)

    
# Print CRT
for row in final_pic:
    print(''.join(row))