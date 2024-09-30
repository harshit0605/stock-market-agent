import requests
from langchain.tools import BaseTool

class StockPriceTool(BaseTool):
    name: str = "Stock Price Tool"
    description: str = "Get the latest stock price for a given ticker symbol from the Indian stock market"
    api_key: str 
    base_url: str = "https://www.alphavantage.co/query"

    def __init__(self, api_key: str):
        super().__init__(api_key=api_key)

    def _run(self, ticker: str) -> str:
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": ticker,
            "apikey": self.api_key
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()

        if "Global Quote" in data:
            latest_price = data["Global Quote"]["05. price"]
            return f"Latest price for {ticker}: ₹{latest_price}"
        else:
            return f"Failed to fetch data for {ticker}. Error: {data.get('Note', 'Unknown error')}"

# Example usage
if __name__ == "__main__":
    api_key = "IKPRCH1Z25YCA2SP"
    tool = StockPriceTool(api_key)
    print(tool._run("RELIANCE.BSE"))  # Example ticker for Reliance Industries on BSE