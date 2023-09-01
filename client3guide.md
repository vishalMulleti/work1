# client3.py

`client3.py` is a Python script that appears to interact with a server API to fetch stock quotes and calculate a price ratio. It contains functions to retrieve data points for stocks and calculate ratios. Below is a brief description of the file and its usage.

## Usage

1. Replace the `QUERY` variable with the API endpoint you want to use. Ensure that the API you are accessing provides stock quotes or the data you require.

2. Make any necessary modifications to the `getDataPoint` function to parse and extract data from the API response. In its current state, it extracts data such as stock symbol, bid price, and ask price.

3. Modify the `getRatio` function to calculate the desired ratio between two prices.

4. Run the script to query the API once every `N` seconds and perform the desired calculations.

## Important Notes

- The script assumes that you have access to a server API that provides stock data. Make sure you have the necessary permissions and API keys if required.

- Depending on your specific use case, you may need to customize the script further to match your requirements.

---

**Disclaimer**: This script serves as a template and may require additional modifications based on the specific API and use case.

---

For any questions or issues, please contact the script author or refer to the API documentation for further assistance.

