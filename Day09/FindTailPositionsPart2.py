with open('SeriesOfMotions.txt', 'r') as f:
    content = f.readlines()

# Define variables
knots = [[0, 0] for _ in range(10)]
moves = {"R": [1, 0], "U": [0, 1], "L": [-1, 0], "D": [0, -1]}
tail_visit = set()


# Move position
def move(dx, dy):
    global knots
    knots[0][0] += dx
    knots[0][1] += dy

    for i in range(1, 10):
        hx, hy = knots[i - 1]
        tx, ty = knots[i]

        if not (abs(hx - tx) <= 1 and abs(hy - ty) <= 1):
            move_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
            move_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tx += move_x
            ty += move_y

        knots[i] = [tx, ty]
        
        
# Loop through each line in the file
for line in content:
    dir, amount = line.split(" ")
    amount = int(amount)
    dx, dy = moves[dir]

    for _ in range(amount):
        move(dx, dy)
        tail_visit.add(tuple(knots[-1]))


print("Number of positions that the tail of the rope visits at least once: ", len(tail_visit))