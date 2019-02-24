from datetime import date, datetime, timedelta


# Date only
date_object = date.today()
print(date_object)

# Date & time
datetime_object = datetime.today()
print(datetime_object)

# Get a date in the future or past:
one_week_and_three_days_ago = datetime.today() - timedelta(weeks=1, days=3)
print(one_week_and_three_days_ago)
