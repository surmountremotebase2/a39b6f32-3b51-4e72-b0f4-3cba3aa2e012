from surmount.base_class import Strategy, TargetAllocation
from surmount.data import Dividend, InstitutionalOwnership
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        # Automatically populate tickers based on predefined criteria
        self.tickers = self.get_high_dividend_stocks()

        # Initialize data objects directly
        self.data_list = [
            Dividend(ticker) for ticker in self.tickers
        ] + [
            InstitutionalOwnership(ticker) for ticker in self.tickers
        ]

    @staticmethod
    def get_high_dividend_stocks():
        # Placeholder for a dynamic query or API call to fetch high-dividend stocks
        return ["AAPL", "MSFT", "JNJ", "PG"]

    @property
    def interval(self):
        return "1day"  # Daily analysis for this strategy

    @property
    def assets(self):
        return self.tickers  # List of tickers

    @property
    def data(self):
        return self.data_list  # Return initialized data objects

    def run(self, data):
        # Initialize equal allocation across assets
        allocation_dict = {ticker: 1 / len(self.tickers) for ticker in self.tickers}

        # Analyze the data
        for data_obj in self.data_list:
            key = (data_obj.__class__.__name__.lower(), data_obj.ticker)

            # Validate if data is available
            if not data.get(key):
                log(f"Warning: No data available for {data_obj.ticker}. Review allocation.")

        # Placeholder for advanced allocation logic
        return TargetAllocation(allocation_dict)