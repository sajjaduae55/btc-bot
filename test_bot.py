import os
import ccxt

print("Bot Started...")

# API Keys from GitHub Secrets
api_key = os.getenv('BINANCE_API_KEY')
api_secret = os.getenv('BINANCE_SECRET')

try:
    # Binance connection
    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret,
        'enableRateLimit': True,
        'options': {'defaultType': 'spot'}
    })
    
    # Get BTC Price
    ticker = exchange.fetch_ticker('BTC/USDT')
    print(f"BTC Price is: {ticker['last']}")

    # Check Balance if keys are present
    if api_key:
        balance = exchange.fetch_balance()
        usdt = balance['free'].get('USDT', 0)
        print(f"USDT Balance: {usdt}")
        print("Bot is LIVE and Connected to Binance!")
    else:
        print("API Keys not found")

except Exception as e:
    print(f"Error: {e}")

print("Bot Finished - OK")
