# Game of Life Visualization

## Overview
This Python script visualizes Conway's Game of Life using NumPy and Matplotlib. The Game of Life is a cellular automaton where cells evolve based on simple rules.

## Features
- Generates a random initial grid of cells.
- Simulates the Game of Life for a given number of iterations.
- Animates the evolution of the cells using Matplotlib.

## Dependencies
- NumPy
- Matplotlib

## Usage
To run the simulation, simply execute the script. The initial grid and number of iterations are predefined but can be modified as needed.

```python
grid = np.random.choice([0, 1], size=(50, 50), p=[0.8, 0.2])
num_iterations = 100
animate_game_of_life(grid, num_iterations)
