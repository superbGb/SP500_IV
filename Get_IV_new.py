import yfinance as yf
import pandas as pd
import numpy as np


class Get_IV:
    def __init__(self,ticker_symbol):
        """
        Initialize the Get_IV object with the ticker symbol of the stock.
        """
        self.ticker_symbol = ticker_symbol
        self.ticker = yf.Ticker(ticker_symbol)


    def get_latest_price(self):
        """
        Fetch the latest price of the stock.
        """
        try:
            # Attempt to fetch the latest price
            latest_price = self.ticker.history(period="1d")["Close"].iloc[-1]
            print(self.ticker.history(period="1d"))
            print(f"Latest price of {self.ticker_symbol}: ${latest_price}")
        except IndexError:
            # If an IndexError is caught, it likely means no data was returned
            print(f"No data available for {self.ticker_symbol}. The ticker might be invalid or data is not accessible.")
    
    def calculate_value(self, expiry_date, today_date):
        """
        Calculate the value of a straddle option strategy.
        """
        try:
            latest_price = self.ticker.history(period="1d")["Close"].iloc[-1]
            options_chain = self.ticker.option_chain(expiry_date)
            num_days_until_expiry = np.busday_count(pd.to_datetime(today_date).date(),pd.to_datetime(expiry_date).date())
            real_expiry_date = expiry_date
            
        except Exception as e:
            option_dates = self.ticker.options
            expiry_date_dt = pd.to_datetime(expiry_date)
            future_dates = [date for date in option_dates if pd.to_datetime(date) > expiry_date_dt]
            next_nearest_date = min(future_dates, key=lambda x: abs(pd.to_datetime(x) - pd.to_datetime(expiry_date)))
            num_days_until_expiry = np.busday_count(pd.to_datetime(today_date).date(),pd.to_datetime(expiry_date).date())
            real_expiry_date = next_nearest_date
            options_chain = self.ticker.option_chain(next_nearest_date)
        
        calls = options_chain.calls
        puts = options_chain.puts

        # Sort the strike list by their proximity to the latest_price
        sorted_strikes = sorted(calls['strike'], key=lambda x: abs(x - latest_price))

        # Initialize variables
        nearest_calls = None
        nearest_puts = None

        # Loop through the sorted strikes
        for strike in sorted_strikes:
            # Check if there's a non-null value for the current strike
            nearest_calls = calls[calls['strike'] == strike][['strike', 'lastPrice']].dropna()
            nearest_puts = puts[puts['strike'] == strike][['strike', 'lastPrice']].dropna()
            
            # If we find a non-null value, break the loop
            if not nearest_calls.empty and not nearest_puts.empty:
                nearest_strike = strike
                break

        # Now nearest_calls and nearest_puts should contain data or remain empty if no suitable strikes exist

        if not nearest_calls.empty and not nearest_puts.empty:
            value = nearest_calls['lastPrice'].iloc[0] + nearest_puts['lastPrice'].iloc[0] + latest_price - nearest_strike
            return round(latest_price,1), round(value,1),real_expiry_date, num_days_until_expiry
        else:
            return round(latest_price,1), "N/A",real_expiry_date, num_days_until_expiry
        
if __name__ == '__main__':



    ticker = 'WMT'
    expiry_date = "2025-02-21"
    date = "2024-12-19"

    # Test

    Stock = yf.Ticker(ticker)
    Latest_price = Stock.history(period="1d")["Close"].iloc[-1]
    print(Latest_price)

    get_iv = Get_IV(ticker)
    price, iv_value, real_expiry_date, days_until_expiry = get_iv.calculate_value(expiry_date,date)

# 50.6


    print(price)
    print(iv_value)
    print(days_until_expiry)
        
        
    