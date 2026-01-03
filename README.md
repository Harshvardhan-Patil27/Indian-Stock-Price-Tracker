PROJECT TITLE: Indian Stock Price Tracker

OVERVIEW This Python tool fetches real-time stock market data for Indian companies (NSE). Instead of web scraping HTML, it consumes a public JSON API endpoint to ensure high speed and data reliability. It is designed to track stocks like TCS, Reliance, and Infosys programmatically.

KEY FEATURES

Live Data Fetching: Connects to the Yahoo Finance API to get up-to-the-minute stock prices.

JSON Parsing: Navigates complex nested JSON structures to extract specific metadata (Price, Currency).

Header Management: Implements custom HTTP headers to bypass basic anti-bot restrictions.

Dynamic Querying: Accepts any NSE stock symbol (e.g., "RELIANCE", "TATAMOTORS") as input.

TECHNICAL STACK

Language: Python 3.x

Library: Requests (HTTP Client)

Data Format: JSON

HOW IT WORKS The script sends an HTTP GET request to the finance endpoint with a stock symbol. It receives a JSON response, parses the nested dictionary to locate the regularMarketPrice key, and displays the formatted result to the user.
