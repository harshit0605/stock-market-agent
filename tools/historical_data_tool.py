import yfinance as yf
from datetime import datetime, timedelta
from langchain.tools import BaseTool
from typing import Literal
from pydantic import Field

import requests
from datetime import datetime, timedelta
from langchain.tools import BaseTool

# class HistoricalDataTool(BaseTool):
#     name = "Historical Data Tool"
#     description = "Get historical stock data for a given ticker symbol"
#     api_key = "YOUR_ALPHA_VANTAGE_API_KEY"  # Replace with your actual API key

#     def _run(self, ticker: str) -> str:
#         # Fetch historical data for the past 30 days
#         end_date = datetime.now()
#         start_date = end_date - timedelta(days=30)
#         start_date_str = start_date.strftime('%Y-%m-%d')
#         end_date_str = end_date.strftime('%Y-%m-%d')
        
#         # Use Alpha Vantage to get the historical data
#         url = f"https://www.alphavantage.co/query"
#         params = {
#             "function": "TIME_SERIES_DAILY",
#             "symbol": ticker,
#             "apikey": self.api_key,
#             "outputsize": "compact"
#         }
#         response = requests.get(url, params=params)
#         data = response.json()
        
#         # Check if the response contains the expected data
#         if "Time Series (Daily)" not in data:
#             return "Error fetching data from Alpha Vantage"
        
#         time_series = data["Time Series (Daily)"]
        
#         # Prepare the data in the desired format
#         historical_data = ["date,price,volume"]
#         for date in sorted(time_series.keys()):
#             if start_date_str <= date <= end_date_str:
#                 day_data = time_series[date]
#                 historical_data.append(f"{date},{day_data['4. close']},{day_data['5. volume']}")
        
#         return "\n".join(historical_data)


class HistoricalDataTool(BaseTool):
    name: Literal["Historical Data Tool"] = Field("Historical Data Tool")
    description: Literal["Get historical stock data for a given ticker symbol"] = Field("Get historical stock data for a given ticker symbol")
    

    def _run(self, ticker: str) -> str:
        # Fetch historical data for the past 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        
        # Use yfinance to get the historical data
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        
        # Prepare the data in the desired format
        data = ["date,price,volume"]
        for date, row in stock_data.iterrows():
            data.append(f"{date.strftime('%Y-%m-%d')},{row['Close']:.2f},{int(row['Volume'])}")
        
        return "\n".join(data)
    
# Example usage
if __name__ == "__main__":
    api_key = "IKPRCH1Z25YCA2SP"
    # tool = HistoricalDataTool(api_key=api_key)
    tool = HistoricalDataTool()
    print(tool._run("IBM"))  # Example ticker for Reliance Industries on BSE