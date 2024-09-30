"""
This is the state definition for the AI.
It defines the state of the agent and the state of the conversation.
"""

from typing import List, TypedDict, Optional
from langgraph.graph import MessagesState

class AgentState(MessagesState):
    """
    This is the state of the agent.
    It is a subclass of the MessagesState class from langgraph.
    """
    ticker : str
    collected_data: Optional[str]
    historical_data: Optional[str]
    risk_report: Optional[str]
    portfolio_report: Optional[str]
    recommendation: Optional[str]
    final_recommendation: Optional[str]
