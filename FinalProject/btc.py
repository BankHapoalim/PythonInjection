from urllib import request
from datetime import date, timedelta
from json import loads


def build_btc_api_url(last_n_days=30):
    end = date.today() - timedelta(days=1)
    start = date.today() - timedelta(days=last_n_days)
    return "https://api.coindesk.com/v1/bpi/historical/close.json?start=%s&end=%s" % (start, end)


def get_last_n_days_closing(last_n_day=30):
    json_btc_data = request.urlopen(build_btc_api_url(last_n_day))
    btc_data = loads(json_btc_data.read())['bpi']
    return list(btc_data.values())


def get_current_rate():
    json_btc_data = request.urlopen("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
    btc_data = loads(json_btc_data.read())['bpi']['USD']
    return btc_data['rate_float']


if __name__ == "__main__":
    print(get_last_n_days_closing())
    print(get_current_rate())
