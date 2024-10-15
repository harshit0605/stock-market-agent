from typing import Dict, Any
from stock_market_agent.models.personas.financial_agent import AdaptiveWeightingSystem
from stock_market_agent.config.state import AgentState2


def integrate_weighted_analyses(state: AgentState2, adaptiveWeightObj : AdaptiveWeightingSystem) -> Dict[str, Any]:
    print("...................In integrate_weighted_analyses node..................")

    market_conditions = state.get('market_conditions',None)
    analyses = state.get("analyses",None)
    if market_conditions is None or analyses in [None, []]:
        return {"combined_weighted_analysis": ""}
    
    
    decisions = {"Buy": 0, "Hold": 0, "Sell": 0}
    total_confidence = 0
    individual_analyses = []

    # Update weights based on the market conditions
    adaptiveWeightObj.update_weights(market_conditions)
    # Get the new weights
    weights = adaptiveWeightObj.weights

    for analysis in analyses:
        agent_name = analysis['agent']
        agent_analysis = analysis['analysis']
        weight = weights.get(agent_name, 1.0)
        
        weighted_confidence = agent_analysis['confidence'] * weight
        decisions[agent_analysis['decision']] += weighted_confidence
        total_confidence += weight

        individual_analyses.append({
            "agent": agent_name,
            "decision": agent_analysis['decision'],
            "confidence": agent_analysis['confidence'],
            "weighted_confidence": weighted_confidence,
            "reasoning": agent_analysis['reasoning']
        })

    # Sort individual analyses by weighted confidence
    individual_analyses.sort(key=lambda x: x['weighted_confidence'], reverse=True)

    # Normalize decision scores
    for decision in decisions:
        decisions[decision] /= total_confidence

    final_decision = max(decisions, key=decisions.get)
    final_confidence = decisions[final_decision]


    # Compile reasoning summary
    reasoning_summary = f"Decision based on Adaptive weighting of the differnet agent personas: {final_decision.upper()} with confidence {final_confidence}\n"
    reasoning_summary += "Integrated Analysis Summary:\n"

    for idx, analysis in enumerate(individual_analyses, 1):
        reasoning_summary += f"{idx}. {analysis['agent']} ({analysis['decision'].upper()}, confidence: {analysis['weighted_confidence']:.2f}):\n"
        reasoning_summary += f"   {analysis['reasoning']}\n\n"

    return {
        "combined_weighted_analysis": reasoning_summary
    }
