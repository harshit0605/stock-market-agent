import numpy as np
from typing import Dict, List, Tuple
from stock_market_agent.models.indicators.base_indicator import BaseIndicator

class MACD(BaseIndicator):
    def __init__(self, short_period: int = 12, long_period: int = 26, signal_period: int = 9):
        self.short_period = short_period
        self.long_period = long_period
        self.signal_period = signal_period

    def calculate(self, prices: List[float]) -> Dict[str, float]:
        prices_array = np.array(prices)
        short_ema = self._ema(prices_array, self.short_period)
        long_ema = self._ema(prices_array, self.long_period)
        macd_line = short_ema - long_ema
        signal_line = self._ema(macd_line, self.signal_period)
        macd_histogram = macd_line - signal_line
        
        return {
            "MACD Line": macd_line[-1],
            "Signal Line": signal_line[-1],
            "MACD Histogram": macd_histogram[-1]
        }

    def _ema(self, prices: np.ndarray, period: int) -> np.ndarray:
        return np.convolve(prices, np.ones(period)/period, mode='valid')
    
    # mean, upper, lower = bb.calculate(prices)
    # financial_data["Bollinger Mean"] = mean[-1]  # Use the latest value
    # financial_data["Bollinger Upper"] = upper[-1]
    # financial_data["Bollinger Lower"] = lower[-1]