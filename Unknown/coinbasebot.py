import ccxt
import time
exchange = ccxt.coinbase({
    'apiKey': '',
    'secret': '',
})

symbols = ['XCN/USD', 'TOSHI/USD', 'BTC/USD']
order_type = 'market'
side = 'buy'
amount = [104, 3000, 0.00001]
order_price = [0.0185, 0.00055, 107000]
done = 0

# Function 1
def buyBTC(symbol, amount, order_price, latest_price):
    global done
    if latest_price < order_price:
        print(f'Ordering {amount:.6f}, of {symbol}, priced at {order_price}')
        order = exchange.create_order(symbol, order_type, side, amount, order_price)
        done += 1
        print(f'New Balance: {balance["USD"]}')
        time.sleep(5)
        return
    else:
        number_Format = latest_price - order_price
        print(f'Latest price: {latest_price:.6f}, too high for order price: {order_price}')
        print(f'Needs: ${number_Format:.6f} less,\n')

# Function 2
def buyTOSHI(symbol, amount, order_price, latest_price):
    global done
    if latest_price < order_price:
        print(f'Ordering {amount}, of {symbol}, priced at {order_price}')
        order = exchange.create_order(symbol, order_type, side, amount, order_price)
        done += 1
        print(f'New Balance: {balance["USD"]}')
        time.sleep(5)
        return
    else:
        number_Format = latest_price - order_price
        print(f'Latest price: {latest_price:.6f}, too high for order price: {order_price}')
        print(f'Needs: ${number_Format:.6f} less,\n')

# Function 3
def buyXCN(symbol, amount, order_price, latest_price):
    global done
    if latest_price < order_price:
        print(f'Ordering {amount}, of {symbol}, priced at {order_price}')
        order = exchange.create_order(symbol, order_type, side, amount, order_price)
        done += 1
        print(f'New Balance: {balance["USD"]}')
        time.sleep(5)
        return
    else:
        number_Format = latest_price - order_price
        print(f'Latest price: {latest_price:.6f}, too high for order price: {order_price}')
        print(f'Needs: ${number_Format:.6f} less,\n')
        
# Function 4
def placeHolder():
    for symbol in symbols:
        if symbol == symbols[0]:
            latest_price = ticker(symbol)
            buyXCN(symbol, amount[0], order_price[0], latest_price)
        elif symbol == symbols[1]:
            latest_price = ticker(symbol)
            buyTOSHI(symbol, amount[1], order_price[1], latest_price)
        elif symbol == symbols[2]:
            latest_price = ticker(symbol)
            buyBTC(symbol, amount[2], order_price[2], latest_price)
    
# Function 5        
def ticker(symbol):
    ticker = exchange.fetch_ticker(symbol)
    ticker_price = ticker['last']
    return ticker_price

while True:
    # Balance
    balance = exchange.fetch_balance()
    print("_______________________________________")
    print(f"\nUSD: {balance['USD']}\n")  # Confirm balance
    try:
        if done == 1:
            print("Project successful.")
            break
        else:
            placeHolder()
            # buyBTC(symbol, amount[2])
            # I was going by line, until this for loop came along to hit all three that are in an array?
            # buyBTC()
            time.sleep(3)
    except Exception as err:
        print(err)
    except ccxt.NetworkError as e:
        print(f"Network Error: {e}")
        time.sleep(5)
        