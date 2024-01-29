# TD1 of decentralization technologies.
### Made by Jack Heger
## game_of_life

#### Description :
The Game of Life is a cellular automaton devised by mathematician John Conway, in which cells evolve based on simple rules and their neighbors' states, creating complex and emergent patterns.

#### How to run the program :
1. In your terminal run : 
git clone https://github.com/jackheger/game_of_life-HEGER-CDOF5.git

2. Again in the terminal run the command : 
python game.py

3. Enjoy and watch the game of life begin !


## Features
- Generates a random initial grid of cells.
- Simulates the Game of Life for a given number of iterations.
- Animates the evolution of the cells using Matplotlib.

## Dependencies
- NumPy
- Matplotlib

'''python
grid = np.random.choice([0, 1], size=(50, 50), p=[0.8, 0.2])
num_iterations = 100
animate_game_of_life(grid, num_iterations)


