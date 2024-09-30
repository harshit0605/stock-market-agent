from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from models.custom_rules_engine import CustomRulesEngine
from models.historical_analysis import HistoricalAnalysis
from models.evaluation_data import EvaluationData

def analysis_agent(state):
    collected_data = state["collected_data"]
    historical_data = state["historical_data"]

    # Extract financial data from collected_data
    financial_data = collected_data["Financial Indicators"]
    sentiment_data = collected_data["Sentiment"]
    
    # Parse collected data (you'll need to implement proper parsing)
    # financial_data = {
    #     "P/E Ratio": "20.5",
    #     "Short-term MA": "105",
    #     "Long-term MA": "100",
    #     "Average Volume": "1000000",
    #     "Current Volume": "1200000",
    #     "RSI": "55",
    #     "Profit Margin": "12",
    #     # Add other indicators here
    # }

    # Perform historical analysis
    analysis = HistoricalAnalysis(historical_data)
    trend = analysis.calculate_trend()
    volatility = analysis.calculate_volatility()
    support, resistance = analysis.identify_support_resistance()
    volume_trend = analysis.volume_trend()
    momentum = analysis.price_momentum()

    # Add historical analysis results to financial data 
    financial_data.update({
        "Price Trend": str(trend),
        "Volatility": str(volatility),
        "Support Level": str(support),
        "Resistance Level": str(resistance),
        "Volume Trend": volume_trend,
        "Price Momentum": momentum,
        "Current Price": str(analysis.data["price"][-1])
    })

    # Create EvaluationData object
    evaluation_data = EvaluationData(financial_data, sentiment_data)

    # Apply custom rules
    rules_engine = CustomRulesEngine()
    rule_results = rules_engine.evaluate(evaluation_data)
    
    # llm = ChatOpenAI(model="gpt-4o")

    # analysis_prompt = f"""
    # Based on the following data, historical analysis and weighted rule-based recommendations, provide a final buy, hold, or sell recommendation:

    # Collected Data:
    # {collected_data}

    # Historical Analysis Results:
    # - Price Trend: {trend:.4f}
    # - Volatility: {volatility:.4f}
    # - Support Level: {support:.2f}
    # - Resistance Level: {resistance:.2f}
    # - Volume Trend: {volume_trend}
    # - Price Momentum: {momentum}

    # Weighted Rule-Based Recommendations:
    # {', '.join(rule_results)}

    # Please consider both the quantitative data and the weighted rule-based recommendations in your analysis.
    # Explain your reasoning, taking into account the confidence levels for each action (Buy, Sell, Hold).
    # Discuss any potential risks or opportunities you see, and how the weights of different rules affected the final recommendation.
    # """
    
    # analysis = llm.invoke([HumanMessage(content=analysis_prompt)])

    return {
        "financial_data": financial_data,
        "sentiment_data": sentiment_data,
        "rule_results": rule_results
    }