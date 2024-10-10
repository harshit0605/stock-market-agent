from typing import Any, Dict, List
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.language_models.chat_models import BaseChatModel

from stock_market_agent.models.schemas import InvestmentDecision
from stock_market_agent.config.state import AgentState

class LLMFinancialAgent:
    def __init__(self, 
            name: str, 
            traits: Dict[str, Any], 
            strategy: List[str], 
            focus: List[str], 
            llm,
            additional_data: Dict[str, Any] = None):
        self.name : str = name
        self.traits: str = traits
        self.strategy: str = strategy
        self.focus: str = focus
        self.additional_data = additional_data or {}
        self.llm: BaseChatModel= llm.with_structured_output(InvestmentDecision)
        self.prompt: PromptTemplate = self._create_prompt()
        self.chain  = self.prompt | self.llm 

    def _create_prompt(self) -> PromptTemplate:
        template = """
        You are a {name}, an AI financial analyst with the following traits:
        {traits}

        Your investment strategy involves:
        {strategy}

        You focus on the following key areas when analyzing stocks:
        {focus}

        Given the following market data:
        {market_data}

        Analyze the data and provide your investment recommendation. Your response should include:
        1. Your decision (buy, sell, or hold)
        2. Your confidence level in this decision (0-1)
        3. A brief explanation of your reasoning

        Response Format:
        Decision: [Your decision]
        Confidence: [Your confidence level]
        Reasoning: [Your explanation]
        """

        return PromptTemplate(
            input_variables=["name", "traits", "strategy", "focus", "market_data"],
            template=template
        )

    def analyze(self, agent_state: AgentState) -> Dict[str, Any]:
        print(f"...................In {self.name} node..................")

        traits_str = "\n".join(f"- {k}: {v}" for k, v in self.traits.items())
        strategy_str = "\n".join(f"- {s}" for s in self.strategy)
        focus_str = "\n".join(f"- {f}" for f in self.focus)
        
        # Extract keys from additional_data to fetch corresponding values from agent_state
        keys_to_include = self.additional_data.get("keys", [])
        # print(f"In {self.name} ----------> Keys to include {keys_to_include}")

        market_data_str = "\n".join(
            f"- {key}: {agent_state.get(key, 'No data available.')}"
            for key in keys_to_include
        )

        input_data = {
            "name": self.name,
            "traits": traits_str,
            "strategy": strategy_str,
            "focus": focus_str,
            "market_data": market_data_str
        }

        response = self.chain.invoke(input_data)

        return {
            "analyses":[
                {
                    "agent" : self.name,
                    "analysis" : {
                        "decision": response.decision,
                        "confidence": response.confidence,
                        "reasoning": response.reasoning
                    }                       
                }
            ]
        }
    
class AdaptiveWeightingSystem:
    def __init__(self, personas):
        self.personas = personas
        self.weights = {persona.name: 1/len(personas) for persona in personas}

    def update_weights(self, market_conditions: Dict[str, Any]):
        for persona in self.personas:
            self.weights[persona.name] = self._calculate_persona_relevance(persona, market_conditions)
        
        # Normalize weights
        total = sum(self.weights.values())
        self.weights = {k: v/total for k, v in self.weights.items()}

    def _calculate_persona_relevance(self, persona, market_conditions):
        # Implement logic to calculate relevance based on market conditions
        # This is a simplified example
        if market_conditions.get('volatility') == 'high' and persona.traits.get('risk_tolerance') == 'Low':
            return 1.5  # Increase weight for conservative investors in volatile markets
        elif market_conditions.get('trend') == 'bullish' and 'growth' in persona.focus:
            return 1.3  # Increase weight for growth-focused investors in bullish markets
        # ... add more conditions ...
        return 1.0  # Default weight
    
class FinancialAgent:
    # def __init__(self, name, risk_tolerance, time_horizon):
    #     self.name = name
    #     self.risk_tolerance = risk_tolerance
    #     self.time_horizon = time_horizon
    
    def __init__(self, name: str, traits: Dict[str, Any], strategy: List[str], focus: List[str]):
        self.name = name
        self.traits = traits
        self.strategy = strategy
        self.focus = focus
        self.confidence = 0.5
        self.success_rate = 0.5

    def adjust_risk(self, market_volatility):
        if market_volatility > self.volatility_threshold:
            self.risk_tolerance *= 0.9  # Reduce risk in volatile markets
        else:
            self.risk_tolerance *= 1.1  # Increase risk in stable markets
        self.risk_tolerance = max(0.1, min(1.0, self.risk_tolerance))  # Keep within bounds

    # If stability and the ability to analyze past decisions are more important (e.g., long-term investment strategies), the historical approach might be more suitable

    # def update_success_rate(self, decision, outcome):
    #     self.past_decisions.append((decision, outcome))
    #     if len(self.past_decisions) > 100:
    #         self.past_decisions.pop(0)
    #     self.success_rate = sum(1 for d, o in self.past_decisions if d == o) / len(self.past_decisions)

    # In scenarios where recent performance is more critical (e.g., high-frequency trading), the exponential moving average might be preferable due to its responsiveness.

    def update_success_rate(self, decision: str, outcome: str):
        # Update success rate based on decision outcome
        self.success_rate = 0.9 * self.success_rate + 0.1 * (decision == outcome)

    def analyze(self, data):
        # Basic analysis logic, to be overridden by specific agents
        return {"decision": "hold", "confidence": self.confidence}

class ValueInvestor(FinancialAgent):
    def analyze(self, data):
        # Conservative-specific analysis
        pass

class MomentumTrader(FinancialAgent):
    def analyze(self, data):
        # Conservative-specific analysis
        pass

class SectorSpecialist(FinancialAgent):
    def analyze(self, data):
        # Conservative-specific analysis
        pass

class GlobalMacroStrategist(FinancialAgent):
    def analyze(self, data):
        # Conservative-specific analysis
        pass
    