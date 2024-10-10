import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "..")))
# print(sys.path)
from stock_market_agent.tools.extract_stock_name import CompanyTickerTool

def get_ticker_node(state):
    print("...................In ticker node..................")
    user_query = state["query"]
    tickers = CompanyTickerTool().run(user_query)

    # company_name = "Apple"
    
    # # Call the symbol search function
    # ticker = search_symbol(company_name)

    if "error" in tickers:
        # Handle the case when the ticker is not found
        return {"error": "Ticker symbol could not be found for the given company name."}

    return {'ticker' : tickers.stock_names[0]}

if __name__ == "__main__":
    print(get_ticker_node({"query" : "Get me the latest financial statements for Apple and Microsoft"}))
    
