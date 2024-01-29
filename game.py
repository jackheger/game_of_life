import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

def game_of_life(grid, num_iterations):
    height, width = grid.shape
    next_grid = np.zeros((height, width))

    for _ in range(num_iterations):
        for i in range(height):
            for j in range(width):
                # Count live neighbors
                live_neighbors = np.sum(grid[max(0, i-1):min(height, i+2), max(0, j-1):min(width, j+2)]) - grid[i, j]

                # Apply the rules of the game
                if grid[i, j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    next_grid[i, j] = 0
                elif grid[i, j] == 0 and live_neighbors == 3:
                    next_grid[i, j] = 1
                else:
                    next_grid[i, j] = grid[i, j]
        
        grid = np.copy(next_grid)
        yield grid

def animate_game_of_life(grid, num_iterations, live_color='black', dead_color='white'):
    fig = plt.figure()
    plt.axis('off')
    ims = []

    # Créer un colormap personnalisé
    cmap = ListedColormap([dead_color, live_color])

    for state in game_of_life(grid, num_iterations):
        im = plt.imshow(state, cmap=cmap, animated=True)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True, repeat_delay=1000)
    plt.show()


grid = np.random.choice([0, 1], size=(50, 50), p=[0.8, 0.2])
num_iterations = 100

# Exemple d'utilisation
animate_game_of_life(grid, num_iterations, live_color='red', dead_color='blue')