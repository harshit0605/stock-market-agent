from typing import Dict, List, Tuple
from models.evaluation_data import EvaluationData


class WeightedRule:
    def __init__(self, rule_func, weight: float):
        self.rule_func = rule_func
        self.weight = weight

# New: Custom Rules Engine

class CustomRulesEngine:
    def __init__(self):
        self.rules = [
            WeightedRule(self.pe_ratio_rule, 0.2),
            WeightedRule(self.moving_average_rule, 0.3),
            WeightedRule(self.volume_spike_rule, 0.15),
            WeightedRule(self.rsi_rule, 0.25),
            WeightedRule(self.profit_margin_rule, 0.1),
            WeightedRule(self.trend_rule, 0.15),
            WeightedRule(self.support_resistance_rule, 0.15),
            WeightedRule(self.sentiment_rule, 0.2),  # New sentiment rule
            # Add more weighted rules as needed
        ]

    def pe_ratio_rule(self, data: EvaluationData) -> Tuple[str, float]:
        pe_ratio = float(data.financial_data['P/E Ratio'])
        if pe_ratio < 15: #(Low P/E Ratio)
            return "Buy", 1.0
        elif pe_ratio > 30: #(High P/E Ratio)
            return "Sell", 1.0
        return "Hold", 0.5 #(P/E Ratio in normal range)

    def moving_average_rule(self, data: EvaluationData) -> Tuple[str, float]:
        # Simulated moving averages
        short_ma = float(data.financial_data['Short-term MA'])
        long_ma = float(data.financial_data['Long-term MA'])
        difference = (short_ma - long_ma) / long_ma
        if difference > 0.05: # (Short-term MA above Long-term MA)
            return "Buy", 1.0
        elif difference < -0.05: # (Short-term MA below Long-term MA)
            return "Sell", 1.0
        return "Hold", 0.5 # (Moving Averages are neutral)

    def volume_spike_rule(self, data: EvaluationData) -> Tuple[str, float]:
        avg_volume = float(data.financial_data['Average Volume'])
        current_volume = float(data.financial_data['Current Volume'])
        if current_volume > (1.5 * avg_volume): #(Significant volume increase)
            return "Buy", 1.0
        elif current_volume < (0.5 * avg_volume):
            return "Sell", 0.8
        return "Hold", 0.3 #(Normal trading volume)

    def rsi_rule(self, data: EvaluationData) -> Tuple[str, float]:
        rsi = float(data.financial_data['RSI'])
        if rsi > 70:
            return "Sell", 1.0 #(Overbought condition)"
        elif rsi < 30:
            return "Buy", 1.0 #(Oversold condition)
        return "Hold", 0.5 #(RSI in neutral range)

    def profit_margin_rule(self, data: EvaluationData) -> Tuple[str, float]:
        profit_margin = float(data.financial_data['Profit Margin'])
        if profit_margin > 20:
            return "Buy", 0.8
        elif profit_margin < 5:
            return "Sell", 0.8
        return "Hold", 0.4
    
    def trend_rule(self, data: EvaluationData) -> Tuple[str, float]:
        trend = float(data.financial_data['Price Trend'])
        if trend > 0.1:
            return "Buy", 1.0
        elif trend < -0.1:
            return "Sell", 1.0
        return "Hold", 0.5
    
    def support_resistance_rule(self, data: EvaluationData) -> Tuple[str, float]:
        current_price = float(data.financial_data['Current Price'])
        support = float(data.financial_data['Support Level'])
        resistance = float(data.financial_data['Resistance Level'])
        
        if current_price < support * 1.05:
            return "Buy", 0.8
        elif current_price > resistance * 0.95:
            return "Sell", 0.8
        return "Hold", 0.5
    
    def sentiment_rule(self, data: EvaluationData) -> Tuple[str, float]:
        sentiment = data.financial_data.get("Sentiment", "Neutral")
        if sentiment == "Positive":
            return "Buy", 1.0
        elif sentiment == "Negative":
            return "Sell", 1.0
        return "Hold", 0.5

    def evaluate(self, data: EvaluationData) -> Dict[str, float]:
        results = {"Buy": 0, "Sell": 0, "Hold": 0}
        total_weight = sum(rule.weight for rule in self.rules)

        for weighted_rule in self.rules:
            action, confidence = weighted_rule.rule_func(data)
            results[action] += weighted_rule.weight * confidence

        # Normalize results
        for action in results:
            results[action] /= total_weight

        return results