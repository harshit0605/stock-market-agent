import numpy as np
from typing import List, Tuple

class MACD:
    def __init__(self, short_period: int = 12, long_period: int = 26, signal_period: int = 9):
        self.short_period = short_period
        self.long_period = long_period
        self.signal_period = signal_period

    def calculate(self, prices: List[float]) -> Tuple[List[float], List[float], List[float]]:
        prices_array = np.array(prices)
        short_ema = self._ema(prices_array, self.short_period)
        long_ema = self._ema(prices_array, self.long_period)
        macd_line = short_ema - long_ema
        signal_line = self._ema(macd_line, self.signal_period)
        macd_histogram = macd_line - signal_line
        
        return macd_line.tolist(), signal_line.tolist(), macd_histogram.tolist()

    def _ema(self, prices: np.ndarray, period: int) -> np.ndarray:
        return np.convolve(prices, np.ones(period)/period, mode='valid')