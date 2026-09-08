🐀 Snake EATS
A small Pygame-based reinforcement learning project where a Q-learning agent learns to move around a 2D arena, avoid obstacles, and catch randomly spawning enemies.

The project started as a simple Pygame game and was extended into an RL experiment using a tabular Q-learning agent.

🎮 What the Game Does
Controls a player in a 1000 × 800 arena.

A rat/enemy spawns at a random location.

An obstacle is placed in the arena.

The AI chooses between:

Stop

Up

Left

Right

Down

Catching the enemy gives a large positive reward.

Moving closer to the enemy gives a smaller positive reward.

Colliding with an obstacle gives a negative reward.

The enemy respawns after being caught.

Training runs for multiple episodes and records:

Episode reward

Average kills per episode

Q-table size

🧠 Reinforcement Learning
The project uses tabular Q-learning.

State
The agent observes seven values:

Distance to the enemy

Enemy direction on the X-axis

Enemy direction on the Y-axis

Distance to the nearest obstacle on the left

Distance to the nearest obstacle above

Distance to the nearest obstacle on the right

Distance to the nearest obstacle below

Continuous distance values are discretized before being used as Q-table keys.

Actions
The action space contains five actions:

0 → Stop
1 → Up
2 → Left
3 → Right
4 → Down
Reward
The current reward design is approximately:

Catch enemy          +50
Move closer          +1
Hit obstacle         -2
The reward is reset after each AI decision so that each Q-learning update receives the reward associated with the corresponding decision interval.

📈 Training Results
The agent has been trained for 50,000 episodes.

The current experiment shows:

Episode reward trending upward.

Q-table growing as new states are encountered.

Average kills per episode increasing substantially during training.

The latest experiment reached roughly 0.7–0.8 average kills per episode, showing a clear improvement compared with the beginning of training.

Note: "kill rate" in the plots currently represents average kills per episode, not the percentage probability of getting a kill.

🗂️ Project Structure
A typical project layout is:

Snake EATS/
│
├── main.py
├── Player.py
├── Ai_agent.py
│
└── Sprites/
    ├── Player Icon.png
    ├── rat.png
    ├── warning.png
    └── Icon.png
The main game imports:

from Player import player
from Ai_agent import Ai_agent
and loads its graphics from the Sprites directory.

⚙️ Requirements
Python 3.x with:

Pygame

NumPy

Matplotlib

tqdm

Install the dependencies with:

pip install pygame numpy matplotlib tqdm
▶️ Running the Project
Make sure the project structure and sprite paths are preserved, then run the main Python file:

python main.py
The training loop will run through the configured number of episodes and display the training graphs when finished.

🔧 Current Q-Learning Configuration
The current agent configuration is:

Agent = Ai_agent(
    0.9,      # Initial epsilon
    0.0001,   # Epsilon decay
    0.1,      # Minimum epsilon
    0.9,      # Learning rate
    0.9       # Discount factor
)
The agent uses an epsilon-greedy policy:

High epsilon → more exploration

Lower epsilon → more exploitation of learned Q-values

📊 Training Graphs
Three metrics are currently plotted:

Reward Distribution
A moving average of episode rewards. An upward trend generally indicates that the agent is receiving better cumulative rewards.

Q-Table Size
Shows the number of unique states stored in the Q-table over training.

A growing Q-table means the agent is encountering new states; Q-table size alone is not a measure of how well the agent is learning.

Average Kills per Episode
Shows the moving average number of enemies caught in each episode.

This is currently the most direct performance metric for the game's objective.

🚧 Future Improvements
Possible next steps:

Add multiple obstacles.

Add moving enemies.

Improve the state representation.

Experiment with learning rate and discount factor.

Compare different reward functions.

Save and load the trained Q-table.

Add a separate visual mode for watching the trained agent.

Add a proper game-over condition.

Compare trained performance against a random agent.

Create a smoother visualization of training progress.

📚 Purpose
This project is primarily a learning experiment in:

Python

Pygame

Reinforcement Learning

Q-learning

State representation

Reward shaping

Exploration vs. exploitation

Training evaluation

It is intended as a hands-on demonstration of how an agent can learn a behavior from rewards rather than being explicitly programmed with a fixed strategy.

Built with Python + Pygame + Q-learning 🐀🤖
