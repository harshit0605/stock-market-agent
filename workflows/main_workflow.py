from langgraph.graph import StateGraph, START, END
from agents.data_collection_agent import data_collection_agent
from agents.analysis_agent import analysis_agent
from agents.risk_assessment_agent import risk_assessment_agent
from agents.portfolio_analysis_agent import portfolio_analysis_agent
from agents.final_recommendation_agent import final_recommendation_agent
from agents.historical_data_agent import historical_data_agent
from tools.historical_data_tool import HistoricalDataTool
from config.state import AgentState

def create_workflow():
    # Updated workflow to include historical data
    workflow = StateGraph(AgentState)
    workflow.add_node("data_collection", data_collection_agent)
    workflow.add_node("historical_data", historical_data_agent)
    workflow.add_node("analysis", analysis_agent)
    # workflow.add_node("risk_assessment", risk_assessment_agent)
    # workflow.add_node("portfolio_analysis", portfolio_analysis_agent)
    workflow.add_node("final_recommendation", final_recommendation_agent)

    workflow.set_entry_point("data_collection")
    workflow.add_edge("data_collection", "historical_data")
    workflow.add_edge("historical_data", "analysis")
    # workflow.add_edge("analysis", "risk_assessment")
    # workflow.add_edge("risk_assessment", "portfolio_analysis")
    # workflow.add_edge("portfolio_analysis", "final_recommendation")
    workflow.add_edge("analysis", "final_recommendation")

    return workflow

# def create_workflow():
    workflow = SequentialGraph()
    workflow.add_node("data_collection", DataCollectionAgent().process)
    workflow.add_node("analysis", AnalysisAgent().process)
    workflow.add_node("risk_assessment", RiskAssessmentAgent().process)
    workflow.add_node("portfolio_analysis", PortfolioAnalysisAgent().process)
    workflow.add_node("final_recommendation", FinalRecommendationAgent().process)

    workflow.set_entry_point("data_collection")
    workflow.add_edge("data_collection", "analysis")
    workflow.add_edge("analysis", "risk_assessment")
    workflow.add_edge("risk_assessment", "portfolio_analysis")
    workflow.add_edge("portfolio_analysis", "final_recommendation")

    return workflow