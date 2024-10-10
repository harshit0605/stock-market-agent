from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field

class StockName(BaseModel):
    stock_names: List[str] = Field(description="The list of stock name mentioned in the query")

class StockTicker(BaseModel):
    companyName : str = Field(description="The name of the company mentioned in the query")
    tickerId : str = Field(description="The alphavantage API compatible ticker id associated with the stock")

class Stocks(BaseModel):
    stock_names: List[StockTicker] = Field(description="The list of stock name and ticker ids mentioned in the user query")

class CompanySelection(BaseModel):
    selected_index: int = Field(description="The index of the selected company from the list of best matches, starting from 1.")

class InvestmentDecision(BaseModel):
    decision : str = Field(description="Your decision (buy, sell, or hold)")
    confidence : float = Field(description="Your confidence level in this decision (0-1)")
    reasoning: str = Field(description="A brief explanation of your reasoning")

class FinalInvestmentDecision(BaseModel):
    final_decision : str = Field(description="A final investment decision (buy, sell, or hold)")
    confidence : str = Field(description="A confidence level for this decision (0-1)")
    reasoning: str = Field(description="A comprehensive reasoning for your decision, taking into account the various perspectives and any conflicts or agreements between the agents")
    additional_insights : str = Field(description="Any additional insights or considerations that might be valuable for the investment decision")