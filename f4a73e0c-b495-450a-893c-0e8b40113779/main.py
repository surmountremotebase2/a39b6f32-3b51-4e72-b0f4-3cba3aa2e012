from surmount.base_class import Strategy, TargetAllocation
from surmount.data import Asset, Dividend, InstitutionalOwnership
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        # Choose assets known for paying steady dividends and displaying lower volatility
        self.tickers = ["AAPL", "MSFT", "JNJ", "PG"]  # Example tickers

        # Initialize data for Dividend and Institutional Ownership for each ticker
        self.data_list = [
            {"type": "dividend", "ticker": ticker, "data": Dividend(ticker)}
            for ticker in self.tickers
        ] + [
            {"type": "institutional_ownership", "ticker": ticker, "data": InstitutionalOwnership(ticker)}
            for ticker in self.tickers
        ]

    @property
    def interval(self):
        # Daily analysis for passive strategy
        return "1day"

    @property
    def assets(self):
        # Return list of tickers
        return self.tickers

    @property
    def data(self):
        # Provide the data initialized for analysis
        return self.data_list

    def run(self, data):
        # Initialize equal allocation across all assets
        allocation_dict = {ticker: 1 / len(self.tickers) for ticker in self.tickers}

        # Analyze dividend and institutional ownership data
        for entry in self.data_list:
            asset_type = entry["type"]
            ticker = entry["ticker"]

            # Check if relevant data is available
            if not data.get((asset_type, ticker)):
                log(f"Warning: No {asset_type} data available for {ticker}. Review allocation.")

        # Placeholder for allocation strategy based on dividend yield and stability
        # Example: Adjust weight towards assets with high dividends and strong institutional ownership
        # allocation_dict["AAPL"] += 0.05  # Sample logic extension

        # Return final allocation decision
        return TargetAllocation(allocation_dict)