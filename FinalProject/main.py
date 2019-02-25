from btc import get_last_n_days_closing, get_current_rate
import statistics
from json import dumps
from datetime import date

last_30_day_closing_rates = get_last_n_days_closing(30)

purchase_price = sum(last_30_day_closing_rates) * 1.02
sell_price = 30 * get_current_rate() * 0.98

balance = sell_price - purchase_price

average = statistics.mean(last_30_day_closing_rates)
variance = statistics.variance(last_30_day_closing_rates)
standard_deviation = statistics.stdev(last_30_day_closing_rates)

stats_dict = {
    'avg': average,
    'var': variance,
    'std_dev': standard_deviation,
    'balance': balance,
}

json_data = dumps(stats_dict)

file_object = open("%s.txt"%date.today(), "w")
file_object.write(json_data)
file_object.close()
