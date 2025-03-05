import pandas as pd
import sqlite3

# Define the CSV file path and SQLite database file path
excel_file = "S&P500 Weights.xlsx"  # Replace with your CSV file path
db_file = "iv_record.db"  # Replace with your SQLite database file name

# Load the CSV file into a Pandas DataFrame
df = pd.read_excel(excel_file)

# Connect to the SQLite database
conn = sqlite3.connect(db_file)

# Load the data into a table in the database
table_name = "SP500_Weight"  # Name for the table
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Define the SQL for the view
view_name = "SP500_Weight"  # Name for the view
view_query = f"""
CREATE VIEW IF NOT EXISTS {view_name} AS
SELECT * FROM {table_name};
"""

# Create the view in the database
cursor = conn.cursor()
cursor.execute(view_query)

# Commit and close the connection
conn.commit()
conn.close()

print(f"View '{view_name}' has been created in the SQLite database '{db_file}'.")