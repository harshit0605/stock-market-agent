from typing import Dict, List, Tuple
from datetime import datetime, timedelta
from scipy import stats
import numpy as np


class HistoricalAnalysis:
    def __init__(self, data: str):
        self.data = self._parse_data(data)

    def _parse_data(self, data: str) -> Dict[str, List[float]]:
        lines = data.strip().split("\n")[1:]  # Skip header
        parsed = {"date": [], "price": [], "volume": []}
        for line in lines:
            date, price, volume = line.split(",")
            parsed["date"].append(datetime.strptime(date, "%Y-%m-%d"))
            parsed["price"].append(float(price))
            parsed["volume"].append(int(volume))
        return parsed

    def calculate_trend(self) -> float:
        x = range(len(self.data["price"]))
        slope, _, _, _, _ = stats.linregress(x, self.data["price"])
        return slope

    def calculate_volatility(self) -> float:
        return np.std(self.data["price"])

    def identify_support_resistance(self) -> Tuple[float, float]:
        prices = self.data["price"]
        support = min(prices)
        resistance = max(prices)
        return support, resistance

    def volume_trend(self) -> str:
        avg_volume_first_half = np.mean(self.data["volume"][:15])
        avg_volume_second_half = np.mean(self.data["volume"][15:])
        if avg_volume_second_half > avg_volume_first_half * 1.1:
            return "increasing"
        elif avg_volume_second_half < avg_volume_first_half * 0.9:
            return "decreasing"
        else:
            return "stable"

    def price_momentum(self) -> str:
        short_term_avg = np.mean(self.data["price"][-5:])
        long_term_avg = np.mean(self.data["price"])
        if short_term_avg > long_term_avg * 1.05:
            return "strong positive"
        elif short_term_avg > long_term_avg:
            return "positive"
        elif short_term_avg < long_term_avg * 0.95:
            return "strong negative"
        elif short_term_avg < long_term_avg:
            return "negative"
        else:
            return "neutral"