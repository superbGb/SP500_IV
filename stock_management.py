import sqlite3
import os
from Implied_Volatility import Implied_Volatility 

class stock_management:
    def __init__(self):
        """
        Initialize the database
        Establish 1 table
        Create function to add next iv_record to the database
        """
        self.db_file = "iv_record.db"
        new_table = self.establish_table()
        if new_table:
            self.current_iv = 0
        else:
            self.current_iv = self.get_current_iv()
        
    def get_current_iv(self):
        '''
        Gets the current highest user_id in use
        Returns 0 if no user's are created
        '''
        coon = sqlite3.connect(self.db_file)
        cursor = coon.cursor()
        cursor.execute("SELECT MAX(iv_index) FROM iv_record")
        try:
            max_iv = cursor.fetchone()[0] + 1 #get the next(current) available id
        except:
            max_iv = 0
        return max_iv
    
    def establish_table(self):
        """Create stock table contains
        [iv_index,date,ticker,iv_value,expiration_date]
        """

        if os.path.exists(self.db_file):
            print("data base exists")
            return False

        else:
            self.create_iv_table()
            print("successfully created IV table")
            return True

    def create_iv_table(self):
        """
        Create Primary Data Table
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS iv_record(
                       iv_index INTEGER PRIMARY KEY,
                       date DATE,
                       sector TEXT,
                       ticker TEXT,
                       price FLOAT,
                       iv_value FLOAT,
                       iv_perc FLOAT,
                       expiration_date DATE,
                       days_until_expiry FLOAT
                       )""")
        conn.commit()
        conn.close()

    def check_duplicate_iv(self,date,ticker,sector, expiry_date):
        """
        check if the iv_record already exists
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT * FROM iv_record WHERE
                       date = ? AND ticker = ? AND sector = ? AND expiration_date = ?
                       """, (date, ticker, sector, expiry_date))
        result = cursor.fetchall()
        conn.close()

        return True if len(result) != 0 else False
    
    def create_iv_record(self,date,sector,ticker,price,iv_value, iv_perc, expiry_date, days_until_expiry):
        """
        create an instance for iv_record
        increment the iv_index
        """
        iv = Implied_Volatility(self.current_iv,date,sector,ticker,price,iv_value, iv_perc, expiry_date, days_until_expiry)
        self.current_iv += 1
        print("successfully created new iv_record")

        return iv
    
    def add_iv_record_to_db(self,iv):
        """
        add iv_record to the database
        """
        exists = self.check_duplicate_iv(iv.date, iv.ticker, iv.sector, iv.expiration_date)

        if not exists:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO iv_record(iv_index ,date ,sector ,ticker ,price ,iv_value ,iv_perc ,expiration_date, days_until_expiry)
                    VALUES({iv.iv_index},'{iv.date}','{iv.sector}','{iv.ticker}','{iv.price}',
                    '{iv.iv_value}','{iv.iv_perc}','{iv.expiration_date}','{iv.days_until_expiry}')""")
            conn.commit()
            conn.close()
            print("successfully added iv_record to the database")
        else:
            print("iv_record already exists")
            self.drop_iv(iv.date, iv.ticker, iv.sector, iv.expiration_date)
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO iv_record(iv_index ,date ,sector ,ticker ,price ,iv_value ,iv_perc ,expiration_date, days_until_expiry)
                    VALUES({iv.iv_index},'{iv.date}','{iv.sector}','{iv.ticker}','{iv.price}',
                    '{iv.iv_value}','{iv.iv_perc}','{iv.expiration_date}','{iv.days_until_expiry}')""")
            conn.commit()
            conn.close()
            print("successfully added iv_record to the database")

    def drop_iv(self, date, ticker, sector, expiry_date):
        """
        Drop an IV by ticker name and date
        """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        #check if record exists
        cursor.execute(f"""SELECT * FROM iv_record WHERE date = ? AND ticker = ? AND sector = ? AND expiration_date = ?""", (date, ticker, sector, expiry_date))
        record = cursor.fetchone()

        if record:
            cursor.execute(f"""DELETE FROM iv_record WHERE date = ? AND ticker = ? AND sector = ? AND expiration_date = ?""", (date, ticker, sector, expiry_date))
            conn.commit()
            print("Successfully delete the record from the database")
        else:
            print("No such record found in the database")
        
        conn.close()
            




    
