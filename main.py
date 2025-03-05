from stock_management import stock_management
from Get_IV_new import Get_IV
import pandas as pd
import json
import time

# Read self-favourite list stocks
with open("/Users/shuaijia/Python/Code/Finance/Tool/Implied Volatility/Finance_2024/tickers_watchlist.json", 'r') as json_file:
    tickers = json.load(json_file)

# Read S&P stocks
SP500_df = pd.read_csv('/Users/shuaijia/Python/Code/Finance/Tool/Implied Volatility/Finance_2024/S&P500 Companies.csv')
SP500_tickers = SP500_df.groupby('Industries')['Ticker'].apply(list).to_dict()
SP500_tickers = {f"{key}_SP500": value for key, value in SP500_tickers.items()}

merged_tickers = {**tickers, **SP500_tickers}


if __name__ == '__main__':
    #Initiate the user object
    # Start the timer
    failed_attempt = []
    start_time = time.time()

    tickers = merged_tickers

    sectors = list(tickers.keys())

    stock = stock_management()
    # expiry_date = "2025-02-14"
    expiry_date = "2025-03-07"
    date = "2025-03-04"

    for sector in sectors:
        tickers_by_sector = tickers[sector]
        for ticker in tickers_by_sector:
            time.sleep(1)
            get_iv = Get_IV(ticker)
            try:
                price, iv_value, real_expiry_date, days_until_expiry = get_iv.calculate_value(expiry_date,date)
                try:
                    iv_perc = round(iv_value,4)/round(price,4)
                except Exception:
                    iv_perc = "N/A"
            except:
                print(f"failed to add the {ticker} to the data base")
                failed_attempt.append(ticker)

            
            try:
                stock1 = stock.create_iv_record(date, sector, ticker ,price , iv_value, round(iv_perc*100,3), real_expiry_date, days_until_expiry)
                stock.add_iv_record_to_db(stock1)
                print(f"{ticker} of {sector} has been added to the database")
            except:
                print(f"failed to add the {ticker} to the data base")
                failed_attempt.append(ticker)

            
    
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(elapsed_time) 

    print(failed_attempt)
    
