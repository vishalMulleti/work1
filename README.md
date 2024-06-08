# About

This project was assigned to me as a task by JP Morgan Chase while I was completing my Vitual-Internship as Software Engineer Intern.


# Stock Price Analysis

This project processes the data feed of stock prices to analyze when trading for the stock should occur. It includes functions to extract relevant data points from stock quotes and to compute the ratio of stock prices.

## Purpose
The main purpose of this project is to process the data feed of stock A and stock B’s prices to enable analysis of when trading for the stock should occur.

## Acceptance Criteria
1. **`getDataPoint` function**: This function should return the correct tuple of stock name, bid_price, ask_price, and price. **Note:** The price of a stock is the average of the bid and ask prices.
2. **`getRatio` function**: This function should return the ratio of the two stock prices.
3. **`main` function**: This function should output correct stock info, prices, and the ratio of the two stock prices.

## Implementation Overview

### `getDataPoint` Function
- Extracts the stock name, bid price, and ask price from a stock quote.
- Calculates the average price of the stock.
- Returns a tuple containing the stock name, bid price, ask price, and the average price.

### `getRatio` Function
- Calculates the ratio of the price of stock A to the price of stock B.
- Handles cases where the price of stock B is zero by returning `None` to avoid division by zero.

### `main` Function
- Defines a list of quotes for stocks A and B.
- Iterates through each quote, processes it using the `getDataPoint` function, and prints the results.
- Calculates and prints the ratio of the prices of stock A and stock B using the `getRatio` function.
