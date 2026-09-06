import numpy as np
import random
from collections import defalutdict



class Ai_agent ():
    def __init__(self, inial_Epsilon:float , Epsilon_decay:float , Final_Epsilon: float , Learning_rate : float , Discount_Factor  : float , ):
        self.Q_value = defalutdict(lambda : np.zeros(5))
        self.epsilon = inial_Epsilon
        self.epsilon_decay = Epsilon_decay
        self.max_epsilon = Final_Epsilon
        self.lr = Learning_rate
        self.discount_factor = Discount_Factor



    def get_action(self,observation) -> int:
        if (random.random()< self.epsilon):
            return random([0,1,2,4,3])