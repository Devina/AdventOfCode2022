with open('SeriesOfMotions.txt', 'r') as f:
    content = f.readlines()

# Define variables
hx, hy = 0, 0
tx, ty = 0, 0
moves = {"R": [1, 0], "U": [0, 1], "L": [-1, 0], "D": [0, -1]}
tail_visit = set()


# Move position
def move(dx, dy):
    global hx, hy, tx, ty

    hx += dx
    hy += dy

    if not (abs(hx - tx) <= 1 and abs(hy - ty) <= 1):
        move_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
        move_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

        tx += move_x
        ty += move_y


# Loop through each line in the file
for line in content:
    dir, amount = line.split(" ")
    amount = int(amount)
    dx, dy = moves[dir]

    for _ in range(amount):
        move(dx, dy)
        tail_visit.add((tx, ty))


print("Number of positions that the tail of the rope visits at least once: ", len(tail_visit))