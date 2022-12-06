with open('Datastream.txt', 'r') as f:
    content = f.readlines()

# Define variables
count = 0
first_start_packet_marker = 0

# Loop through each line in the file
for line in content:
    for c in line:  # Accounting for start character
        has_repeated_chars = len(set(line[count:count+14:1])) != len(line[count:count+14:1])  # If repeated characters in the extracted string then is True else False
        if has_repeated_chars:
            count+=1
        else:
            break

first_start_packet_marker = count + 14 # Counter account for point upto when repeated characters. So first instance is distinct characters after.

print("Characters to be processed before the first start-of-message marker is detected: ", first_start_packet_marker)
