def euclidean_steps(x, y):
    steps = 0
    while y != 0:
        x, y = y, x % y
        steps += 1
    return steps

def find_pairs(target_steps):
    for x in range(2, target_steps + 2):
        for y in range(1, x):
            if euclidean_steps(x, y) == target_steps:
                return x, y
    return None

# Datos de ejemplo (cambia estos valores según necesites)
t = 2
target_steps = [1, 3]

pairs = []
for steps in target_steps:
    pair = find_pairs(steps)
    if pair:
        pairs.append(pair)
    else:
        print("No pair found for", steps)

print(" ".join(str(pair) for pair in pairs))