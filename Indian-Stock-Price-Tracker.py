import requests # The tool to make the phone call to the server

def get_stock_price(symbol):
    # 1. Define the URL (The Kitchen)
    # We use the Yahoo Finance hidden API. ".NS" means National Stock Exchange (India).
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}.NS"
    
    # 2. Add Headers (The ID Card)
    # Some servers block Python scripts. We pretend to be a real Browser (User-Agent).
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # 3. Request Data (Ask the Waiter)
        response = requests.get(url, headers=headers)
        
        # 4. Parse JSON (Read the Menu)
        # .json() converts the text response into a Python Dictionary
        data = response.json()
        
        # 5. Extract the Price (Digging into the dictionary)
        # The data is hidden deep inside: chart -> result -> meta -> regularMarketPrice
        price = data['chart']['result'][0]['meta']['regularMarketPrice']
        currency = data['chart']['result'][0]['meta']['currency']
        
        return price, currency

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None

# --- USE THE FUNCTION ---
stock = "RELIANCE" # Try "RELIANCE", "INFY", "TATAMOTORS"
price, currency = get_stock_price(stock)

if price:
    print(f"✅ Current Price of {stock}: {price} {currency}")
else:
    print("❌ Failed to get price.")