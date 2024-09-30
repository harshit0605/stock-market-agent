import requests
from langchain.tools import BaseTool
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pydantic import Field

class NewsSentimentTool(BaseTool):
    name: str = Field(default="News Sentiment Tool", const=True)
    description: str = Field(default="Analyze recent news sentiment for a given company", const=True)
    api_key: str = Field(default="News Sentiment Tool", const=True)
    base_url: str = Field(default="https://newsapi.org/v2/everything", const=True)

    def __init__(self, api_key: str):
        super().__init__(api_key=api_key)
        self.analyzer = SentimentIntensityAnalyzer()

    def _run(self, company: str) -> str:
        params = {
            "q": company,
            "sortBy": "publishedAt",
            "apiKey": self.api_key,
            "language": "en"
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()

        # Debugging information
        print("API Response:", data)

        if "articles" in data:
            sentiments = []
            for article in data["articles"]:
                title = article["title"]
                description = article["description"]
                content = article["content"]
                text = f"{title} {description} {content}"
                sentiment = self.analyzer.polarity_scores(text)
                sentiments.append(sentiment["compound"])

            if sentiments:
                average_sentiment = sum(sentiments) / len(sentiments)
                sentiment_label = "Positive" if average_sentiment > 0 else "Negative" if average_sentiment < 0 else "Neutral"
                return f"Average sentiment for {company}: {sentiment_label} ({average_sentiment:.2f})"
            else:
                return f"No sentiment data available for {company}."
        else:
            return f"Failed to fetch news for {company}. Error: {data.get('message', 'Unknown error')}"

# Example usage
if __name__ == "__main__":
    api_key = "33329b286a8d40c89a39748b2bb98dd5"
    tool = NewsSentimentTool(api_key=api_key)
    print(tool._run("Reliance Industries"))
    