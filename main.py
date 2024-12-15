def manhattan_distance(point1, point2):     # function to calculate he manhattan distance 
  return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


class gridWorld:           # setting up the grid world environment from the player and the goal position 
  def __init__ (self, size = 12):
    self.size = size
    self.player_position = [0, 0]
    self.goal_position = [size -1, size -1]
    self.agent_position = [0, 1]

  def reset(self):
    self.player_position = [0, 0]
    self.agent_position = [0, 1]
    #self.goal_position - [self.size -1, self.size -1]
    return self.player_position, self.agent_position

  def move(self, action):     # player movement around the grid world
    if action == "up":
      self.player_position[0] = max(0, self.player_position[0] -1)
    elif action == "down":
      self.player_position[0] = min(self.size - 1, self.player_position[0] + 1)
    elif action == "left":
      self.player_position[1] = max(0, self.player_position[1] - 1)
    elif action == "right":
      self.player_position[1] = min(self.size - 1, self.player_position[1] + 1)
     
    player_distance_to_goal = manhattan_distance(self.player_position, self.goal_position)   # calculate the player distance to the goal from the initial position
    print(f"Player dustance to goal : {player_distance_to_goal}")


    if self.agent_position[0] < self.agent_position[0]:      # setting the movement of the agent 
      self.agent_position[0] += 1   # move down
    else:
      self.agent_position[1] += 1   # move right
      
    agent_distance_to_goal = manhattan_distance(self.agent_position, self.goal_position)    # calculate the distance from start position of agent to the goal position
    print(f"Agent distance to the goal: {agent_distance_to_goal}")

    player_win = self.player_position == self.goal_position
    agent_win = self.agent_position == self.goal_position

    done  = player_win or agent_win      # chek if the player has alredy reached the goal position or not 
    return self.player_position, done , self.agent_position, agent_win, player_win
    print("I am here")

  def render(self):       # render the environment for agent , player and the goal 
    for i in range(self.size):
      for j in range(self.size):
        if self.player_position == [i, j]:
          print("P", end = " ")
        elif self.agent_position == [i, j]:
          print("A", end = " ")
        elif self.goal_position == [i, j]:
          print("G", end =  " ")
        else:
          print(".", end = " ")

      print()
    print()

def main():      # inference for performin the movement and everythnig in the grid world environment
  environment = gridWorld()
  environment.reset()

  print("Welcome to the grid world: ")
  print("Move the player (P) to the goal (G) using the given keys below :")
  print("'W' for up, 'S' for down, 'A' for left, 'D' for right.")
  print("Press 'Q' to quit.")

  done = False
  while not done:            
    environment.render()
    action = input("Enter the mover: ").lower()
    if action == "q":
      print("Thanks for playing he game!")
      break
    if action in ["w", "a", "s", "d"]:
      action_map = {"w": "up", "s": "down", "a": "left", "d": "right"}
      player_position, done, agent_position, agent_win, player_win = environment.move(action_map[action])

      if player_win:
        environment.render()
        print("Congraulations! You reached the goal!")
      elif agent_win:
        environment.render()
        print("Agent the win.")
    else:
      print("Invalid input! Please use 'W', 'A', 'S', or 'D'.")
if __name__ == "__main__":
  main()

