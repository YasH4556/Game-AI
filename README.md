# 🐀 Snake EATS

> **A 2D Pygame game where a Q-learning agent learns to hunt enemies while avoiding obstacles.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Pygame-Game%20Development-green?style=for-the-badge" alt="Pygame">
  <img src="https://img.shields.io/badge/Reinforcement%20Learning-Q--Learning-orange?style=for-the-badge" alt="Q-learning">
</p>

---

## 🎮 About

**Snake EATS** is a reinforcement learning project built from scratch with Python and Pygame.

Instead of manually programming the player to chase the enemy, the agent learns which actions are useful by interacting with the game and receiving rewards.

The current environment contains:

- 🐀 A randomly positioned enemy
- ⚠️ An obstacle
- 🤖 A Q-learning agent
- 🗺️ A 1000 × 800 game area
- 🔄 Random enemy respawning
- 📊 Training metrics and graphs

The main goal is simple:

> **Learn to catch as many enemies as possible while avoiding obstacles.**

---

## 🧠 How the AI Learns

The agent uses **tabular Q-learning** with an **epsilon-greedy action-selection strategy**.

At each decision:

```text
        Observe the game
              ↓
          Get state
              ↓
       Choose an action
              ↓
         Move player
              ↓
       Receive reward
              ↓
        Observe next state
              ↓
         Update Q-table
```

### State

The agent receives information about:

| Observation | Description |
|---|---|
| Enemy distance | Distance between player and enemy |
| Enemy X direction | Left / same / right |
| Enemy Y direction | Up / same / down |
| Obstacle left | Distance to obstacle on the left |
| Obstacle up | Distance to obstacle above |
| Obstacle right | Distance to obstacle on the right |
| Obstacle down | Distance to obstacle below |

Distance values are discretized before being stored in the Q-table.

### Actions

```text
0 → Stop
1 → Up
2 → Left
3 → Right
4 → Down
```

---

## 🏆 Reward System

The current reward structure encourages the agent to approach and catch the enemy while discouraging obstacle collisions.

| Event | Reward |
|---|---:|
| 🐀 Catch enemy | **+50** |
| 🎯 Move closer to enemy | **+1** |
| ⚠️ Hit obstacle | **−2** |

The reward is reset after each AI decision so that each Q-learning update receives the reward associated with that decision interval.

---

## 📈 Training Results

The latest experiment used:

**50,000 training episodes**

The training graphs show:

### Reward

The moving average of episode reward increases throughout training, indicating that the agent is generally receiving better returns as training progresses.

### Q-table

The Q-table grows as the agent encounters new states.

> A larger Q-table does **not** automatically mean better performance. It mainly indicates that more unique states have been encountered.

### Average Kills per Episode

The most important performance metric for this project is the average number of enemies caught per episode.

The latest training run shows a clear upward trend, reaching roughly:

**~0.7–0.8 kills per episode**

This is a significant improvement compared with the beginning of training.

---

## ⚙️ Current Agent Configuration

```python
Agent = Ai_agent(
    0.9,       # Initial epsilon
    0.0001,    # Epsilon decay
    0.1,       # Minimum epsilon
    0.9,       # Learning rate
    0.9        # Discount factor
)
```

### What these parameters mean

| Parameter | Value | Purpose |
|---|---:|---|
| Initial ε | 0.9 | Starts with lots of exploration |
| ε decay | 0.0001 | Gradually reduces exploration |
| Minimum ε | 0.1 | Keeps some exploration |
| Learning rate α | 0.9 | Controls how strongly new information changes Q-values |
| Discount factor γ | 0.9 | Controls how much future rewards matter |

---

## 🗂️ Project Structure

```text
Snake EATS/
│
├── main.py
├── Player.py
├── Ai_agent.py
├── README.md
│
└── Sprites/
    ├── Icon.png
    ├── Player Icon.png
    ├── rat.png
    └── warning.png
```

---

## 🛠️ Requirements

- Python 3.x
- Pygame
- NumPy
- Matplotlib
- tqdm

Install the dependencies:

```bash
pip install pygame numpy matplotlib tqdm
```

---

## ▶️ Run the Project

Clone/download the project and make sure the `Sprites` folder is in the correct location.

Then run:

```bash
python main.py
```

The program will train the Q-learning agent and display the training graphs after training finishes.

---

## 📊 Training Metrics

The project currently tracks:

```text
Episode Reward
      │
      ├── Measures cumulative reward
      │
Q-table Size
      │
      ├── Measures unique states encountered
      │
Average Kills
      │
      └── Measures actual game performance
```

The graphs use a moving average to make the overall training trend easier to see despite the natural randomness of reinforcement learning.

---

## 🔬 What This Project Demonstrates

This project was built to explore practical reinforcement learning concepts:

- Reinforcement learning
- Q-learning
- Q-tables
- Epsilon-greedy exploration
- Exploration vs. exploitation
- Reward shaping
- State discretization
- Temporal-difference learning
- Training evaluation
- Pygame-based environments

---

## 🚧 Possible Improvements

Future versions could include:

- [ ] Save and load the trained Q-table
- [ ] Add multiple obstacles
- [ ] Add moving enemies
- [ ] Improve the state representation
- [ ] Add a dedicated AI visualization mode
- [ ] Compare the trained agent against a random agent
- [ ] Experiment with different reward functions
- [ ] Tune learning rate and discount factor
- [ ] Add more detailed training statistics
- [ ] Separate the game simulation from rendering for faster training

---

## 💡 Project Goal

The purpose of **Snake EATS** is not just to make a game.

It is an experiment in answering a simple question:

> **Can an agent learn how to play a game from rewards instead of being explicitly programmed with the strategy?**

The current results suggest that it can. 🤖

---

<p align="center">

### 🐀 Built with Python • Pygame • NumPy • Q-learning

**Snake EATS — teaching a tiny AI to chase rats.**

</p>
