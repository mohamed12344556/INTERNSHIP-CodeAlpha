import requests

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] += quantity
        else:
            self.portfolio[symbol] = {'quantity': quantity, 'price': self.get_stock_price(symbol)}

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]['quantity']:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol]['quantity'] -= quantity
        else:
            print(f"{symbol} is not in the portfolio.")

    def get_stock_price(self, symbol):
        # Use Alpha Vantage API to get real-time stock price
        api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'
        endpoint = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        
        try:
            response = requests.get(endpoint)
            data = response.json()
            return float(data['Global Quote']['05. price'])
        except Exception as e:
            print(f"Error getting stock price for {symbol}: {e}")
            return None

    def display_portfolio(self):
        print("Stock Portfolio:")
        for symbol, data in self.portfolio.items():
            print(f"{symbol}: Quantity - {data['quantity']}, Current Price - {data['price']}")

if __name__ == "__main__":
    portfolio_tracker = StockPortfolioTracker()

    # Example: Adding stocks to the portfolio
    portfolio_tracker.add_stock('AAPL', 5)
    portfolio_tracker.add_stock('GOOGL', 3)

    # Display the initial portfolio
    portfolio_tracker.display_portfolio()

    # Example: Removing stocks from the portfolio
    portfolio_tracker.remove_stock('AAPL', 2)

    # Display the updated portfolio
    portfolio_tracker.display_portfolio()
