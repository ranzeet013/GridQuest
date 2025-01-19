# Grid World Game 

## Overview

This project implements a simple **Grid World** game in Python, where the player (P) navigates a grid to reach a goal (G), while avoiding static monsters (M1, M2, M3) placed at different positions. The agent (A) moves towards the goal using the **A\*** algorithm, simulating AI movement in the environment. The player and agent both work independently, and the goal is to either reach the goal or allow the agent to win by reaching it first.

The grid world is designed to provide a simulation of a basic environment with dynamic movement, where obstacles (monsters) and the goal create an interactive challenge for both the player and the agent.

## Features

- **Pathfinding**: The agent uses the A\* algorithm to find the optimal path to the goal while avoiding obstacles (monsters).
- **Player Movement**: The player controls the character in the grid using specific commands (W, A, S, D for movement).
- **Agent Movement**: The agent moves autonomously towards the goal, avoiding static obstacles based on the A\* algorithm.
- **Grid World Setup**: A customizable grid world, with a player, an agent, monsters, and a goal.
- **Collision Handling**: The player and agent are prevented from moving onto monster positions, ensuring safe paths.

## How It Works

The game is played on a **12x12** grid, where:

- **P** represents the player's position.
- **A** represents the agent's position.
- **M1, M2, M3** represent the positions of three static monsters.
- **G** represents the goal.

### Player Movement

The player can move up, down, left, or right using the following keys:

- **W** for up
- **S** for down
- **A** for left
- **D** for right

The player’s goal is to navigate from the start position at the top-left corner to the goal located at the bottom-right corner, avoiding the monsters.

### Agent Movement

The agent uses the **A\*** pathfinding algorithm to autonomously move towards the goal. The agent's movement is calculated based on its current position, the goal's position, and the obstacles (monsters) in the grid. It will avoid moving into the same position as a monster and will attempt to find the optimal path to the goal.

### Game End Conditions

- The game ends when the player reaches the goal (**P reaches G**).
- The agent wins if it reaches the goal (**A reaches G**) before the player.

## Tech Stack

- **Python**: The primary programming language used to implement the game logic.
- **A\*** Algorithm: A pathfinding algorithm used to determine the most optimal path for the agent to reach the goal while avoiding obstacles.
- **Manhattan Distance**: Used as a heuristic in the A\* algorithm to calculate the shortest distance between two points in a grid-based environment.
- **Command-line Interface (CLI)**: The game is played through the terminal with input commands for controlling the player's movements.

## Conclusion
The Grid World Game with A* pathfinding offers an interactive experience, combining player movement with autonomous AI. The agent uses A* to efficiently navigate the grid, avoiding monsters while striving to reach the goal first. This project showcases practical pathfinding application and can be further enhanced with additional features like dynamic obstacles or more complex AI behavior.
