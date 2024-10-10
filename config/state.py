"""
This is the state definition for the AI.
It defines the state of the agent and the state of the conversation.
"""

from typing import Dict, List, TypedDict, Optional, Annotated
from operator import add

from langgraph.graph import MessagesState
from stock_market_agent.models.schemas import Stocks

class AnalysisResult(TypedDict):
    decision: str
    confidence: float
    reasoning: str

class FinalPrediction(TypedDict):
    final_analysis: AnalysisResult
    additional_insights: str

class AgentAnalysis(TypedDict):
    agent: str
    analysis: AnalysisResult

class AgentState(MessagesState):
    """
    This is the state of the agent.
    It is a subclass of the MessagesState class from langgraph.
    """
    query: str
    ticker : Stocks
    collected_data: Optional[str]
    historical_data: Optional[str]
    risk_report: Optional[str]
    portfolio_report: Optional[str]
    recommendation: Optional[str]
    final_recommendation: Optional[str]
    rule_results : Optional[Dict[str, float]]
    error : Optional[str]

class AgentState2(MessagesState):
    """
    This is the state of the agent.
    It is a subclass of the MessagesState class from langgraph.
    """
    query: str
    ticker : Stocks
    stock_price: Optional[str]
    news_sentiment: Optional[str]
    financial_indicators: Optional[str]
    historical_data: Optional[str]
    collected_data: Optional[Dict[str, Dict[str, str]]]
    risk_report: Optional[str]
    portfolio_report: Optional[str]
    # analyses: Optional[Annotated[list[AgentAnalysis], add]]
    analyses: Annotated[list[AgentAnalysis], add]
    combined_weighted_analysis: str
    market_conditions : Optional[Dict[str, str]]
    final_prediction : Optional[FinalPrediction]
    error : Optional[str]
