
def analyze_stock(stock_prices):

    for i in range(3, len(stock_prices)):
        last_3_avg = sum(stock_prices[i-3:i]) / 3
        current_price = stock_prices[i]

        print(f"Analyzing stock price for Day: {i+1}:")
        print(f"Last 3 days average price: {last_3_avg:.2f}, Current price: {current_price:.2f}")

        if current_price > last_3_avg:
            print("Stock price is increasing. BUY STOCK")

        elif current_price < last_3_avg:
            print("Stock price is decreasing. SELL STOCK")

        else:
            print("Stock price is stable. HOLD STOCK")


stock_prices = [100, 110, 120, 111, 70, 170, 110, 106]

analyze_stock(stock_prices)