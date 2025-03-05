class Implied_Volatility:
    def __init__(self,iv_index,date,sector,ticker,price,iv_value,iv_perc, expiry_date,days_until_expiry):
        self.iv_index = iv_index
        self.date = date
        self.sector = sector
        self.ticker = ticker
        self.iv_value = iv_value
        self.expiration_date = expiry_date
        self.days_until_expiry = days_until_expiry
        self.price = price
        self.iv_perc = iv_perc