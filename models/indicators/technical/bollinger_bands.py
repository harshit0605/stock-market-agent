import numpy as np
from typing import List, Tuple

class BollingerBands:
    def __init__(self, period: int = 20, num_std_dev: float = 2.0):
        self.period = period
        self.num_std_dev = num_std_dev

    def calculate(self, prices: List[float]) -> Tuple[List[float], List[float], List[float]]:
        prices_array = np.array(prices)
        rolling_mean = np.convolve(prices_array, np.ones(self.period)/self.period, mode='valid')
        rolling_std = np.array([np.std(prices_array[i:i+self.period]) for i in range(len(prices_array) - self.period + 1)])
        
        upper_band = rolling_mean + (rolling_std * self.num_std_dev)
        lower_band = rolling_mean - (rolling_std * self.num_std_dev)
        
        return rolling_mean.tolist(), upper_band.tolist(), lower_band.tolist()