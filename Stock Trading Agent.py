import random

class StockTradingAgent:
    def __init__(self, risk_tolerance="medium"):
        self.risk_tolerance = risk_tolerance  
        self.price_weight = 0.4  
        self.trend_weight = 0.3  
        self.news_weight = 0.3  

    def get_stock_price_change(self):
        return random.uniform(-5, 5)  

    def get_historical_trend(self):
        return random.choice(["Uptrend", "Downtrend", "Stable"])

    def get_company_news_sentiment(self):
        return random.choice(["Positive", "Negative", "Neutral"])

    def calculate_utility(self, price_change, trend, news):
        price_score = price_change  
        trend_score = 5 if trend == "Uptrend" else -5 if trend == "Downtrend" else 0
        news_score = 5 if news == "Positive" else -5 if news == "Negative" else 0

        total_score = (price_score * self.price_weight) + \
                      (trend_score * self.trend_weight) + \
                      (news_score * self.news_weight)
        return total_score

    def decide_action(self, utility_score):
        if utility_score > 2:
            return "Buy"
        elif utility_score < -2:
            return "Sell"
        else:
            return "Hold"

    def analyze_stock(self, stock_name):
        price_change = self.get_stock_price_change()
        trend = self.get_historical_trend()
        news = self.get_company_news_sentiment()

        utility_score = self.calculate_utility(price_change, trend, news)
        action = self.decide_action(utility_score)

        print(f"Stock: {stock_name}")
        print(f"Price Change: {price_change:.2f}%")
        print(f"Trend: {trend}")
        print(f"News Sentiment: {news}")
        print(f"Utility Score: {utility_score:.2f}")
        print(f"Recommended Action: {action}")
        print("---")

# Run the agent for 5 different stocks
stock_names = ["AAPL", "TSLA", "GOOGL", "AMZN", "MSFT"]
agent = StockTradingAgent(risk_tolerance="medium")

for stock in stock_names:
    agent.analyze_stock(stock)
