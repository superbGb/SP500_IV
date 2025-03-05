tickers = {
    "RPMC": ["HST", "NU", "SPG", "MAA", 
             "ISRG", "NVDA", "WM", "SSNC", "CAH",
             "TSLA", "APPF", "RIVN", "AROC", "PAYO","CPT"],

    "interest": [ 
        "XLRE",
        "IWM", 
        "DHI", 
        "XLU"
    ],
    "commodity": [
        "XLE", 
        "XME", 
        "GDX",
        "OXY",
    ],
    "tech": [
        "GOOG",  # Google
        "TSLA",   # Tesla
        "MSFT",   # Microsoft
        "AMD",    # Advanced Micro Devices
        "NVDA",   # NVIDIA
        "TSM",    # Taiwan Semiconductor Manufacturing Company
        "SOXX",   # iShares PHLX Semiconductor ETF
        "QQQ",
        "SPY",
        "XLK",
        "ASML"
    ],
    "consumption": [
        "RTX",
        "LMT",
        "WM", 
        "XLV", 
        "COST", 
        "TGT",
        "XRT", 
        "XLP",
        "XLY",
        "NKE", 
        "LULU", 
        "DIS"
    ],
    "finance": [
        "BRK-B", 
        "XLF", 
        "IWM"
    ],

    "Nov_Watch":["XRT","TSLA","TSM","IWM","XLV","AMD","SOXX","NVDA","ASML"]
}

import json

json_file_path = "tickers_watchlist.json"
with open(json_file_path, 'w') as json_file:
    json.dump(tickers, json_file, indent=4)

json_file_path