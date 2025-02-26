import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors
import random

EMPTY = -1
TREE = 1
FIRE = 2
BURNED = 0

grid_size = 50
forest = np.random.choice([EMPTY, TREE], size=(grid_size, grid_size), p=[
                          0.2, 0.8])

fire_positions = []
while len(fire_positions) < 3:
    x, y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
    if forest[x, y] == TREE:
        forest[x, y] = FIRE
        fire_positions.append((x, y))


def update(frame):
    global forest
    new_forest = forest.copy()

    for x in range(1, grid_size - 1):
        for y in range(1, grid_size - 1):
            if forest[x, y] == FIRE:
                new_forest[x, y] = BURNED

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if forest[x + dx, y + dy] == TREE:
                        new_forest[x + dx, y + dy] = FIRE

    forest = new_forest
    mat.set_data(forest)
    return [mat]


cmap = mcolors.ListedColormap(["saddlebrown", "black", "green", "red"])
norm = mcolors.BoundaryNorm([EMPTY, BURNED, TREE, FIRE, FIRE+1], cmap.N)

fig, ax = plt.subplots()
mat = ax.matshow(forest, cmap=cmap, norm=norm)
ani = animation.FuncAnimation(
    fig, update, frames=50, interval=200, repeat=False)

plt.show()
