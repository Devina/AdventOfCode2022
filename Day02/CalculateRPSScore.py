with open('EncryptedStrategyGuide.txt', 'r') as f:
    content = f.readlines()

# Define variables
rps_score = 0

# Loop through each combination and add the score along the way
for line in content:
    if 'A X' in line:   # Rock & Rock
        rps_score += 4  # 1 for Rock chosen and 3 for Draw
    elif 'A Y' in line: # Rock & Paper
        rps_score += 8  # 2 for Paper chosen and 6 for Win
    elif 'A Z' in line: # Rock & Scissors
        rps_score += 3  # 3 for Scissors chosen and 0 for Loss
    elif 'B X' in line: # Paper & Rock
        rps_score += 1  # 1 for Rock chosen and 0 for Loss
    elif 'B Y' in line: # Paper & Paper
        rps_score += 5  # 2 for Paper chosen and 3 for Draw
    elif 'B Z' in line: # Paper & Scissors
        rps_score += 9  # 3 for Scissors chosen and 6 for Win
    elif 'C X' in line: # Scissors & Rock
        rps_score += 7  # 1 for Rock chosen and 6 for Win
    elif 'C Y' in line: # Scissors & Paper
        rps_score += 2  # 2 for Paper chosen and 0 for Loss
    elif 'C Z' in line: # Scissors & Scissors
        rps_score += 6  # 3 for Scissors chosen and 3 for Draw
    else:
        pass
        
print("Final Rock Paper Scissors Score: ", rps_score)