from typing import Dict, List
from stock_market_agent.models.indicators.technical.bollinger_bands import BollingerBands
from stock_market_agent.models.indicators.technical.macd import MACD
from stock_market_agent.models.indicators.technical.rsi import RSI
from datetime import datetime

class TechnicalIndicators:
    def __init__(self, data: str):
        self._parsed_data = self._parse_data(data)
        self.prices = self._parsed_data["price"]

    def calculate_indicators(self) -> Dict[str, float]:
        # Calculate Bollinger Bands
        bb = BollingerBands()
        mean, upper, lower = bb.calculate(self.prices)

        # Calculate MACD
        macd = MACD()
        macd_line, signal_line, histogram = macd.calculate(self.prices)

        # Calculate RSI
        rsi = RSI()
        rsi_values = rsi.calculate(self.prices)

        indicators_data = {
            "Bollinger Mean": mean[-1],
            "Bollinger Upper": upper[-1],
            "Bollinger Lower": lower[-1],
            "MACD Line": macd_line[-1],
            "Signal Line": signal_line[-1],
            "MACD Histogram": histogram[-1],
            "RSI": rsi_values[-1]
        }

        return indicators_data

    def _parse_data(self, data: str) -> Dict[str, List[float]]:
        lines = data.strip().split("\n")[1:]  # Skip header
        parsed = {"date": [], "price": [], "volume": []}
        for line in lines:
            date, price, volume = line.split(",")
            parsed["date"].append(datetime.strptime(date, "%Y-%m-%d"))
            parsed["price"].append(float(price))
            parsed["volume"].append(int(volume))
        return parsed