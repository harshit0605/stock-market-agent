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
            # WeightedRule(self.rsi_rule, 0.25),
            WeightedRule(self.profit_margin_rule, 0.1),
            WeightedRule(self.trend_rule, 0.15),
            WeightedRule(self.support_resistance_rule, 0.15),
            WeightedRule(self.sentiment_rule, 0.2),  # New sentiment rule
            WeightedRule(self.volatility_rule, 0.1),  # New volatility rule
            WeightedRule(self.current_price_rule, 0.1),
            WeightedRule(self.operating_cash_flow_rule, 0.1),  # New rule
            WeightedRule(self.free_cash_flow_rule, 0.1),  # New rule
            WeightedRule(self.cash_flow_from_investing_rule, 0.1),  # New rule
            WeightedRule(self.cash_flow_from_financing_rule, 0.1),  # New rule
            WeightedRule(self.net_change_in_cash_rule, 0.1),  # New rule
            # Add more weighted rules as needed
        ]
    
    def pe_ratio_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        pe_ratio = float(data.financial_data['P/E Ratio'])
        if pe_ratio < 15:
            return "Buy", 1.0, f"Low P/E Ratio of {pe_ratio} indicates undervaluation."
        elif pe_ratio > 30:
            return "Sell", 1.0, f"High P/E Ratio of {pe_ratio} indicates overvaluation."
        return "Hold", 0.5, f"P/E Ratio of {pe_ratio} is within normal range."

    def moving_average_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        short_ma = float(data.financial_data['Short-term MA'])
        long_ma = float(data.financial_data['Long-term MA'])
        difference = (short_ma - long_ma) / long_ma
        if difference > 0.05:
            return "Buy", 1.0, f"Short-term MA ({short_ma}) is above Long-term MA ({long_ma})."
        elif difference < -0.05:
            return "Sell", 1.0, f"Short-term MA ({short_ma}) is below Long-term MA ({long_ma})."
        return "Hold", 0.5, "Moving Averages are neutral."

    def volume_spike_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        avg_volume = float(data.financial_data['Average Volume'])
        current_volume = float(data.financial_data['Current Volume'])
        if current_volume > (1.5 * avg_volume):
            return "Buy", 1.0, f"Significant volume increase (Current: {current_volume}, Average: {avg_volume})."
        elif current_volume < (0.5 * avg_volume):
            return "Sell", 0.8, f"Significant volume decrease (Current: {current_volume}, Average: {avg_volume})."
        return "Hold", 0.3, f"Normal trading volume (Current: {current_volume}, Average: {avg_volume})."

    def volatility_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        volatility = float(data.financial_data['Volatility'])
        if volatility > 0.2:
            return "Sell", 0.8, f"High volatility of {volatility}."
        elif volatility < 0.1:
            return "Buy", 0.8, f"Low volatility of {volatility}."
        return "Hold", 0.5, f"Moderate volatility of {volatility}."

    def current_price_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        current_price = float(data.financial_data['Current Price'])
        average_price = float(data.financial_data['Average Price'])
        if current_price < average_price * 0.9:
            return "Buy", 0.7, f"Current price ({current_price}) is significantly lower than average price ({average_price})."
        elif current_price > average_price * 1.1:
            return "Sell", 0.7, f"Current price ({current_price}) is significantly higher than average price ({average_price})."
        return "Hold", 0.5, f"Current price ({current_price}) is close to average price ({average_price})."

    def profit_margin_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        profit_margin = float(data.financial_data['Profit Margin'])
        if profit_margin > 20:
            return "Buy", 0.8, f"High profit margin of {profit_margin}%."
        elif profit_margin < 5:
            return "Sell", 0.8, f"Low profit margin of {profit_margin}%."
        return "Hold", 0.4, f"Moderate profit margin of {profit_margin}%."

    def trend_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        trend = float(data.financial_data['Price Trend'])
        if trend > 0.1:
            return "Buy", 1.0, f"Positive price trend of {trend}."
        elif trend < -0.1:
            return "Sell", 1.0, f"Negative price trend of {trend}."
        return "Hold", 0.5, f"Neutral price trend of {trend}."

    def support_resistance_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        current_price = float(data.financial_data['Current Price'])
        support = float(data.financial_data['Support Level'])
        resistance = float(data.financial_data['Resistance Level'])
        
        if current_price < support * 1.05:
            return "Buy", 0.8, f"Current price ({current_price}) is near support level ({support})."
        elif current_price > resistance * 0.95:
            return "Sell", 0.8, f"Current price ({current_price}) is near resistance level ({resistance})."
        return "Hold", 0.5, f"Current price ({current_price}) is between support ({support}) and resistance ({resistance})."
    
    def sentiment_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        sentiment_info = data.sentiment_data
        sentiment_label = sentiment_info.get("sentiment", "Neutral")
        average_score = sentiment_info.get("average_score", 0.0)

        if sentiment_label == "Positive":
            return "Buy", 1.0, f"Positive sentiment with an average score of {average_score}."
        elif sentiment_label == "Negative":
            return "Sell", 1.0, f"Negative sentiment with an average score of {average_score}."
        return "Hold", 0.5, f"Neutral sentiment with an average score of {average_score}."

    def operating_cash_flow_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        operating_cash_flow = float(data.financial_data.get('Operating Cash Flow'))
        if operating_cash_flow > 0:
            return "Buy", 0.8, f"Positive operating cash flow of {operating_cash_flow}."
        elif operating_cash_flow < 0:
            return "Sell", 0.8, f"Negative operating cash flow of {operating_cash_flow}."
        return "Hold", 0.5, f"Neutral operating cash flow of {operating_cash_flow}."

    def free_cash_flow_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        free_cash_flow = float(data.financial_data['Free Cash Flow'])
        if free_cash_flow > 0:
            return "Buy", 0.8, f"Positive free cash flow of {free_cash_flow}."
        elif free_cash_flow < 0:
            return "Sell", 0.8, f"Negative free cash flow of {free_cash_flow}."
        return "Hold", 0.5, f"Neutral free cash flow of {free_cash_flow}."

    def cash_flow_from_investing_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        cash_flow_from_investing = float(data.financial_data['Cash Flow from Investing'])
        if cash_flow_from_investing < 0:
            return "Buy", 0.6, f"Negative cash flow from investing ({cash_flow_from_investing}), indicating investment in growth."
        elif cash_flow_from_investing > 0:
            return "Sell", 0.6, f"Positive cash flow from investing ({cash_flow_from_investing}), indicating divestment of assets."
        return "Hold", 0.5, f"Neutral cash flow from investing ({cash_flow_from_investing})."

    def cash_flow_from_financing_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        cash_flow_from_financing = float(data.financial_data['Cash Flow from Financing'])
        if cash_flow_from_financing > 0:
            return "Buy", 0.6, f"Positive cash flow from financing ({cash_flow_from_financing}), indicating raising capital."
        elif cash_flow_from_financing < 0:
            return "Sell", 0.6, f"Negative cash flow from financing ({cash_flow_from_financing}), indicating paying off debt."
        return "Hold", 0.5, f"Neutral cash flow from financing ({cash_flow_from_financing})."

    def net_change_in_cash_rule(self, data: EvaluationData) -> Tuple[str, float, str]:
        net_change_in_cash = float(data.financial_data['Net Change in Cash'])
        if net_change_in_cash > 0:
            return "Buy", 0.7, f"Positive net change in cash ({net_change_in_cash})."
        elif net_change_in_cash < 0:
            return "Sell", 0.7, f"Negative net change in cash ({net_change_in_cash})."
        return "Hold", 0.5, f"Neutral net change in cash ({net_change_in_cash})."
    
    def extract_metric(self, rule_func, data: EvaluationData) -> str:
        # Mapping of rule functions to their corresponding metric keys
        rule_to_metrics = {
            self.pe_ratio_rule: ["P/E Ratio"],
            self.moving_average_rule: ["Short-term MA", "Long-term MA"],
            self.volume_spike_rule: ["Current Volume", "Average Volume"],
            self.volatility_rule: ["Volatility"],
            self.current_price_rule: ["Current Price", "Average Price"],
            self.profit_margin_rule: ["Profit Margin"],
            self.trend_rule: ["Price Trend"],
            self.support_resistance_rule: ["Current Price", "Support Level", "Resistance Level"],
            self.sentiment_rule: ["Sentiment"],
            self.operating_cash_flow_rule: ["Operating Cash Flow"],
            self.free_cash_flow_rule: ["Free Cash Flow"],
            self.cash_flow_from_investing_rule: ["Cash Flow from Investing"],
            self.cash_flow_from_financing_rule: ["Cash Flow from Financing"],
            self.net_change_in_cash_rule: ["Net Change in Cash"],
            # Add more mappings as needed
        }

        # Retrieve the metric keys for the given rule function
        metric_keys = rule_to_metrics.get(rule_func, [])

        # Construct the metric string
        metrics = []
        for key in metric_keys:
            if key in data.financial_data:
                metrics.append(f"{key}: {data.financial_data.get(key, 'N/A')}")
            elif key in data.sentiment_data:
                metrics.append(f"{key}: {data.sentiment_data.get(key, 'N/A')}")
        
        return ", ".join(metrics) if metrics else "Metric not available"

    def evaluate(self, data: EvaluationData) -> Dict[str, Dict[str, float]]:
        results = {
            "Buy": {"score": 0, "reasoning": []},
            "Sell": {"score": 0, "reasoning": []},
            "Hold": {"score": 0, "reasoning": []}
        }
        total_weight = sum(rule.weight for rule in self.rules)

        for weighted_rule in self.rules:
            action, confidence, message = weighted_rule.rule_func(data)
            detailed_reasoning = (
                f"Rule: {weighted_rule.rule_func.__name__}\n"
                f"Metric: {self.extract_metric(weighted_rule.rule_func, data)}\n"
                f"Condition: {message}\n"
                f"Confidence: {confidence}\n"
            )
            results[action]["score"] += weighted_rule.weight * confidence
            results[action]["reasoning"].append(detailed_reasoning)

        # Normalize results
        for action in results:
            results[action]["score"] /= total_weight

        # Format the output to be more verbose
        formatted_results = {}
        for action, details in results.items():
            formatted_results[action] = {
                "score": details["score"],
                "reasoning": "\n\n".join(details["reasoning"])
            }

        return formatted_results