# Stock Market Analysis Agent

This project is a comprehensive stock market analysis agent built using the `langgraph` framework. It leverages various agents to collect data, perform analysis, assess risks, and provide final investment recommendations. The system is designed to be modular and extensible, allowing for easy integration of new data sources and analytical methods.

## Features

- **Data Collection**: Gathers financial data, news sentiment, and portfolio information.
- **Historical Analysis**: Analyzes historical stock data to identify trends, volatility, and support/resistance levels.
- **Risk Assessment**: Evaluates the risk associated with the portfolio, including beta, Sharpe ratio, and diversification.
- **Portfolio Analysis**: Provides insights into the portfolio's value, largest holdings, and sector allocations.
- **Final Recommendation**: Generates a comprehensive investment recommendation based on collected data and analysis.

## Agents

### Data Collection Agent

Collects various types of data including stock prices, news sentiment, financial indicators, and portfolio data.

### Historical Data Agent

Fetches and processes historical stock data for trend analysis and volatility calculation.

### Analysis Agent

Performs detailed analysis on the collected data, including financial indicators and historical trends.

### Risk Assessment Agent

Assesses the risk of the portfolio by calculating metrics like beta, Sharpe ratio, and diversification.

### Portfolio Analysis Agent

Analyzes the portfolio to provide insights into its value, largest holdings, and sector allocations.

### Final Recommendation Agent

Generates a final investment recommendation based on all collected and analyzed data.

## Custom Rules Engine

The custom rules engine allows for fine-tuned control over the investment recommendations. It evaluates various financial indicators and sentiment data to provide weighted rule-based recommendations.

### Example Rules

- **P/E Ratio Rule**: Recommends actions based on the P/E ratio.
- **Moving Average Rule**: Uses short-term and long-term moving averages to make recommendations.
- **Volume Spike Rule**: Detects significant changes in trading volume.
- **RSI Rule**: Uses the Relative Strength Index to identify overbought or oversold conditions.
- **Sentiment Rule**: Incorporates news sentiment into the recommendation process.

## Historical Analysis

The historical analysis component is crucial for understanding past performance and predicting future trends. It includes:

- **Trend Calculation**: Identifies the overall price trend.
- **Volatility Calculation**: Measures the stock's price volatility.
- **Support and Resistance Levels**: Identifies key price levels.
- **Volume Trend**: Analyzes changes in trading volume.
- **Price Momentum**: Assesses the momentum of the stock price.

## Workflow

The main workflow orchestrates the execution of various agents to provide a comprehensive analysis and recommendation.

## Getting Started

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Ensure you have the necessary API keys set up in your environment.

4. **Run the main script**:
   ```sh
   python main.py
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## License

This project is licensed under the MIT License.
