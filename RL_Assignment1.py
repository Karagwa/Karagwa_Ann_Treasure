import numpy as np
import random

# environment setup
road_length = 8  # Positions: 0 (start) to 7 (goal)
actions=["left", "right"]

# Q-table (state x action)
Q = np.zeros((road_length, len(actions)))


# Define the learning parameters
episodes = 1000  # Number of episodes :# How many times the agent will try to learn where each episode is a complete run from start to goal
learning_rate = 0.8 # Learning rate :# How fast the agent learns, the higher it is, the faster the agent learns and the more it forgets previous knowledge
gamma = 0.9  # Discount factor      :When it is high, the agent values future rewards more
epsilon = 0.3  # Exploration rate   :# 30% of the time, the agent will choose a random action instead of the best known action

# Training loop
for episode in range(episodes):
    state = 0  # Start at position 0

    while state != 7:  # Goal is position 7
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:  # if the random number choosen between 0 and 1 is less than epsilon, the agent will choose a random action ie between 0 and 1
            action = random.randint(0, 1)  # Explore (random action)
        else:
            action = np.argmax(Q[state])  # Q[state] gives the Q-values for the current state, np.argmax(Q[state]) returns the index of the action with the highest Q-value (best known action)

        # Take action and get new state
        if action == 0:  # Move left
            new_state = max(0, state - 1)
        else:  # Move right
            new_state = min(7, state + 1)

        # Reward: +1 if reached goal, else 0
        reward = 1 if new_state == 7 else 0

        # Q-learning update rule
        Q[state, action] = Q[state, action] + learning_rate * (reward + gamma * np.max(Q[new_state]) - Q[state, action])

        # Move to new state
        state = new_state
        
        
"""
Traing loop explanation:
1. For each episode, the agent starts at position 0.
2. The agent selects an action based on the epsilon-greedy policy:
   - With probability epsilon, it chooses a random action (exploration).  Initially, this allows the agent to explore different actions and learn about the environment.
   - Otherwise, it chooses the action with the highest Q-value for the current state (exploitation).
3. The agent takes the selected action, which results in a new state.
4. If the new state is the goal (position 4), it receives a reward of 1; otherwise, the reward is 0.
5. The Q-value for the current state-action pair is updated using the Q-learning formula, which incorporates the reward received and the maximum Q-value of the new state.
6. The agent transitions to the new state and continues until it reaches the goal.
"""
        
# Display learned Q-table
print("Learned Q-table:")
print(Q)

# Test the trained agent
state = 0
steps = 0
path = []
print("\nAgent's path to cross the road:")
while state != 7:
    action = np.argmax(Q[state])  # Choose best action
    if action == 0:
        state = max(0, state - 1)
        path.append("left")
    else:
        state = min(7, state + 1)
        path.append("right")
    steps += 1
    
print(f"Steps taken: {steps}")
print(f"Path taken: {path}")
print(f"Final position: {state}")
