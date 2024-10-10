from tools.historical_data_tool import HistoricalDataTool
from tools.news_sentiment_tool import NewsSentimentTool
from tools.financial_indicators_tool import FinancialIndicatorsTool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage, AIMessage
import os

def data_collection_node(state):
    print("...................In data_collection_node node..................")
    stock_price = state["stock_price"]
    news_sentiment = state["news_sentiment"]
    financial_indicators = state["financial_indicators"]

    return {
        "collected_data" : {
            "stock_price" : stock_price,
            "news_sentiment" : news_sentiment,
            "financial_indicators" : financial_indicators
        }
    }