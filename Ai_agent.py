import numpy as np
import random
from collections import defaultdict

action_space = (0 , 1 ,2 ,3 ,4)

class Ai_agent ():
    def __init__(self, inial_Epsilon:float , Epsilon_decay:float , Final_Epsilon: float , Learning_rate : float , Discount_Factor  : float , ):
        self.Q_value = defaultdict(lambda : np.zeros(len(action_space)))
        self.epsilon = inial_Epsilon
        self.epsilon_decay = Epsilon_decay
        self.max_epsilon = Final_Epsilon
        self.lr = Learning_rate
        self.discount_factor = Discount_Factor



    def get_action(self,observation) -> int:
        if (random.random()< self.epsilon):
            return int(random.choice(action_space))
        else:
            return int(np.argmax(self.Q_value[observation]))

    def Update(self ,action :int,reward: int, obs: tuple, Next_obs : tuple , truncated :bool):
        if truncated:
            target = reward

        else:
            target = reward + self.discount_factor*np.max(self.Q_value[Next_obs])

        temporal_diff = target - self.Q_value[obs][action]
        self.Q_value[obs][action] += self.lr*temporal_diff

        return False

    def decay_epsilon(self):
            self.epsilon = max(self.max_epsilon, self.epsilon - self.epsilon_decay)