from tools.stock_price_tool import StockPriceTool
from tools.news_sentiment_tool import NewsSentimentTool
from tools.financial_indicators_tool import FinancialIndicatorsTool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage, AIMessage
from tools.portfolio_tool import PortfolioTool
import os

def data_collection_agent(state):
    ticker = state["ticker"]

    news_api_key = os.getenv("YOUR_NEWS_API_KEY")
    if not news_api_key:
        raise ValueError("No YOUR_NEWS API key found. Please set the YOUR_NEWS_API_KEY environment variable.")
    
    alphavantage_api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not alphavantage_api_key:
        raise ValueError("No ALPHA_VANTAGE API key found. Please set the ALPHA_VANTAGE_API_KEY environment variable.")

    # Use tools to collect data
    stock_price_tool = StockPriceTool(api_key=alphavantage_api_key)
    news_sentiment_tool = NewsSentimentTool(api_key=news_api_key)
    search_tool = DuckDuckGoSearchRun()
    financial_indicators_tool = FinancialIndicatorsTool(api_key=alphavantage_api_key)

    price_info = stock_price_tool.run(ticker)
    sentiment_info = news_sentiment_tool.run(ticker)
    recent_news = search_tool.run(f"{ticker} stock recent news")
    financial_indicators = financial_indicators_tool.run(ticker)

    portfolio_data = PortfolioTool().run()

    collected_data = {
        "Stock Price": price_info,
        "Sentiment": sentiment_info,
        "Financial Indicators": financial_indicators,
        "portfolio_data" : portfolio_data
    }
    
    return {
        "messages": state["messages"] + [AIMessage(content=str(collected_data))],
        "collected_data": collected_data
    }