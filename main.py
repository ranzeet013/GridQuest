import heapq

def manhattan_distance(point1, point2):       # calculating the manhattan distance working on the grid world 
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def a_star(start, goal, grid_size, monster_positions):    #  applying the a star algo fro the agent to move in the grid world
    def is_valid(pos):
        return 0 <= pos[0] < grid_size and 0 <= pos[1] < grid_size and pos not in monster_positions

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]    # direction to move up down left right 

    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_cost = {start: 0}
    f_cost = {start: manhattan_distance(start, goal)}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]   # reverse the path from goal to start

        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])

            if not is_valid(neighbor):
                continue

            tentative_g_cost = g_cost[current] + 1

            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = tentative_g_cost
                f_cost[neighbor] = tentative_g_cost + manhattan_distance(neighbor, goal)
                heapq.heappush(open_list, (f_cost[neighbor], neighbor))

    return None  # No path found

class gridWorld:       # setting up the grid world
    def __init__(self, size=12):
        self.size = size
        self.player_position = [0, 0]     # player position
        self.goal_position = [size - 1, size - 1]    # goal position
        self.agent_position = [0, 1]  # agnt position
        self.monster1_position = [4, 4]   # m1, m2 and 3 monsters positions
        self.monster2_position = [8, 8]
        self.monster3_position = [8, 4]

    def reset(self):         # reset the world 
        self.player_position = [0, 0]
        self.agent_position = [0, 1]
        self.monster1_position = [4, 4]
        self.monster2_position = [8, 8]
        self.monster3_position = [8, 4]
        return self.player_position, self.agent_position, self.monster1_position, self.monster2_position, self.monster3_position

    def move(self, action):   # setting the movement for the player
        if action == "up":
            self.player_position[0] = max(0, self.player_position[0] - 1)
        elif action == "down":
            self.player_position[0] = min(self.size - 1, self.player_position[0] + 1)
        elif action == "left":
            self.player_position[1] = max(0, self.player_position[1] - 1)
        elif action == "right":
            self.player_position[1] = min(self.size - 1, self.player_position[1] + 1)

        player_distance_to_goal = manhattan_distance(self.player_position, self.goal_position)   # calculaing the manhattan distance fom the player position to goal position
        print(f"Player distance to goal: {player_distance_to_goal}")

        path = a_star(tuple(self.agent_position), tuple(self.goal_position), self.size, [     # applying the a star algorithm to move the agnt in the grid world
            tuple(self.monster1_position), tuple(self.monster2_position), tuple(self.monster3_position)])

        if path and len(path) > 1:
            self.agent_position = list(path[1])

        agent_win = False
        if self.agent_position == self.goal_position:
            agent_win = True
        else:
            agent_distance_to_goal = manhattan_distance(self.agent_position, self.goal_position)    # calculating the manhattan distance from agent position to the goal position
            print(f"Agent moved to: {self.agent_position}, Agent distance to the goal: {agent_distance_to_goal}")

        player_win = self.player_position == self.goal_position
        done = player_win or agent_win
        return self.player_position, done, self.agent_position, agent_win, player_win

    def render(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.player_position == [i, j]:
                    print("P", end=" ")
                elif self.agent_position == [i, j]:
                    print("A", end=" ")
                elif self.monster1_position == [i, j]:
                    print("M1", end=" ")
                elif self.monster2_position == [i, j]:
                    print("M2", end=" ")
                elif self.monster3_position == [i, j]:
                    print("M3", end=" ")
                elif self.goal_position == [i, j]:
                    print("G", end=" ")
                else:
                    print(".", end=" ")

            print()
        print()

def main():
    environment = gridWorld()
    environment.reset()

    print("Welcome to the grid world: ")
    print("M1, M2 and M3 represents the monsters position which are static.")
    print("Move the player (P) to the goal (G) using the given keys below :")
    print("'W' for up, 'S' for down, 'A' for left, 'D' for right.")
    print("Press 'Q' to quit.")

    done = False
    while not done:
        environment.render()
        action = input("Enter the move: ").lower()
        if action == "q":
            print("Thanks for playing the game!")
            break
        if action in ["w", "a", "s", "d"]:
            action_map = {"w": "up", "s": "down", "a": "left", "d": "right"}
            player_position, done, agent_position, agent_win, player_win = environment.move(action_map[action])

            if player_win:
                environment.render()
                print("Congratulations! You reached the goal!")
            elif agent_win:
                environment.render()
                print("Agent wins.")
        else:
            print("Invalid input! Please use 'W', 'A', 'S', or 'D'.")

if __name__ == "__main__":
    main()
