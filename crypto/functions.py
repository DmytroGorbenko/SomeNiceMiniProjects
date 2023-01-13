from pycoingecko import CoinGeckoAPI
import datetime


GEKO = CoinGeckoAPI()


def percent(prev: float, curr: float):
    if prev > curr:
        differ = "-" + str(round(100 - curr / prev * 100, 3))
    else:
        differ = "+" + str(round(100 - prev / curr * 100, 3))
    return differ


def weekly_info(currency: str):
    curr_time = datetime.datetime.now()
    week_delta = datetime.timedelta(days=7, hours=1)
    week_ago = curr_time - week_delta

    curr_time = str(datetime.datetime.timestamp(curr_time))
    week_ago = str(datetime.datetime.timestamp(week_ago))

    try:
        week_info = GEKO.get_coin_market_chart_range_by_id(currency.lower(), "usd", week_ago, curr_time)
    except Exception as e:
        print(e)
        return 1

    prev_price = week_info["prices"][0][1]

    print(f"Currency: {currency.upper()}")
    for i in range(24, 169, 24):
        price = week_info["prices"][i][1]
        percentage = percent(prev_price, price)
        market = week_info["market_caps"][i][1]
        volume = week_info["total_volumes"][i][1]

        unix_time = week_info["prices"][i][0] / 1000
        human_time = datetime.datetime.fromtimestamp(unix_time)
        human_time = human_time.strftime('%Y-%m-%d %H:%M:%S')

        print(f"Date: {human_time}")
        print(f"Price: {price:-20}$ | Market cap: {market:-20}$ | Volume: {volume:-20}$ | Change(24h): {percentage}%")
        print()
        prev_price = price


weekly_info("bitcoin")
