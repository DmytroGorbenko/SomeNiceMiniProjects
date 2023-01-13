import yahoo_fin.stock_info as si
from datetime import datetime, timedelta
import requests


def convert_currency(first_curr, sec_curr, scr_amount):
    symbol = f"{first_curr}{sec_curr}=X"
    time = datetime.now()

    try:
        data = si.get_data(symbol, interval="1m", start_date=datetime.now() - timedelta(days=2))
    except AssertionError:
        print("Functionality if your input is correct and try again!")
        return time.ctime(), None

    price = data.iloc[-1].close
    return time.ctime(), price * scr_amount


def usd_to_btc(usd_amount):

    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(key)
    data = data.json()
    usd_price = float(data["price"])

    res = round(usd_amount / usd_price, 5)
    return res


def btc_to_usd(btc_amount):

    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(key)
    data = data.json()
    usd_price = float(data["price"])

    return round(usd_price * btc_amount, 5)


MENU = " 1 - Convert to BTC.\n 2 - Convert from BTC\n 3 - Exit."

if __name__ == "__main__":
    print("Welcome to the bitcoin converter!")
    while True:

        print()
        print("Choose the variant:", MENU, sep='\n')
        choice = input("Your choice: ")

        if choice == "3":
            print("Thanks for using our app! See you later!")
            exit(0)

        elif choice == "1":
            source_currency = input("Enter the currency you wand to convert into BTC: ").upper()

            while True:
                try:
                    amount = float(input("Enter the amount: "))
                    if amount < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input value! Enter again please!")

            curr_time, exchange_rate = convert_currency(source_currency, "USD", amount)
            if exchange_rate is None:
                continue

            value = usd_to_btc(exchange_rate)

            print(f"At this moment: {curr_time}")
            print(f"{amount} {source_currency} equals {value} BTC")

        elif choice == "2":
            while True:
                try:
                    btc = float(input("Enter the amount: "))
                    if btc < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input value! Enter again please!")

            currency = input("Enter the currency to convert into: ")

            usd = btc_to_usd(btc)
            curr_time, exchange_rate = convert_currency("USD", currency, usd)
            if exchange_rate is None:
                continue

            print(f"At this moment: {curr_time}")
            print(f"{btc} BTC equals {exchange_rate} {currency}")

        else:
            print("This variant does not exist! Enter again!")
