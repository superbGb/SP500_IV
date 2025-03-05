# Finance_2024

# Stock Implied Volatility Tracker

## Introduction

This `main.py` script is designed to calculate and store the **implied volatility (IV)** of stocks, including both **user-favorite stocks** and **all S&P 500 companies**, categorized by industry. The script fetches stock prices and IV values, computes IV as a percentage of the stock price, and saves the data in a database for further analysis.

### Key Features:
1. **Load Stock Lists**: Reads a JSON file containing the user’s favorite stocks and a CSV file with S&P 500 stocks grouped by industry.
2. **Initialize Objects**: Creates an instance of `stock_management` for managing stock records and `Get_IV` for retrieving implied volatility.
3. **Process Stocks**:
   - Iterates over all sectors and stocks in the dataset.
   - Retrieves the stock price and IV for a given expiry date.
   - Computes IV as a percentage of the stock price.
   - Stores the calculated values in a database.
4. **Handle Failures**: Tracks stocks for which IV retrieval fails and prints a list at the end.
5. **Execution Time Measurement**: Logs the time taken for the entire process.

---

## Prerequisites

Ensure you have the following installed in your Python environment:

- **Python 3.x**
- Required Python packages: `pandas`, `json`, `time`
- **`stock_management`** module for database operations
- **`Get_IV`** module for fetching implied volatility

Additionally, you need:

- A JSON file (`tickers_watchlist.json`) listing your favorite stocks.
- A CSV file (`S&P500 Companies.csv`) containing S&P 500 stock tickers and their industry classifications.

---

## How to Use

### 1. Prepare Your Files
- Ensure **`tickers_watchlist.json`** and **`S&P500 Companies.csv`** are stored in the specified directory.
- The **JSON file** should contain stock tickers categorized into groups.
- The **CSV file** should include **S&P 500 tickers** with their corresponding **industries**.

### 2. Run the Script
To execute the script, run the following command:

```bash
python main.py
```

### 3. Understanding the Parameters
The script uses two important date parameters:

- **`expiry_date`**: The target expiry date for the options contracts (e.g., `"2025-03-07"`).
- **`date`**: The current reference date (e.g., `"2025-03-04"`).

You can modify these values inside the script to suit your analysis.

### 4. Results
- Successfully processed stocks are **added to the database**.
- If a stock **fails to retrieve IV data**, it will be **logged in `failed_attempt`**.

### 5. Execution Time
At the end, the script prints:
- **Total execution time** in seconds.
- **List of failed stock retrievals**.

---

## Example Output

```plaintext
AAPL of Technology_SP500 has been added to the database
GOOGL of Communication Services_SP500 has been added to the database
failed to add TSLA to the database
...
Total execution time: 120.45 seconds
Failed attempts: ['TSLA', 'NVDA']
```

---

## Customization

- **Modify Expiry Date**: Change `expiry_date` in the script to analyze different option contracts.
- **Update Stock Lists**: Edit `tickers_watchlist.json` or `S&P500 Companies.csv` to include/exclude stocks.
- **Adjust Sleep Time**: Modify `time.sleep(1)` to control API request frequency.
- **Error Handling**: Enhance exception handling to log errors more effectively.

---

## Troubleshooting

| Issue                     | Possible Solution |
|---------------------------|------------------|
| **Missing JSON/CSV File** | Ensure the files exist in the correct directory. |
| **Database Connection Issues** | Verify that the `stock_management` module is correctly set up. |
| **IV Retrieval Failures** | Some tickers may not have available options data. Try a different expiry date. |

---

## Conclusion

This script **automates the retrieval, calculation, and storage of stock implied volatility data**, making it useful for traders and analysts tracking market volatility trends.

---

### Author
**David Jia**