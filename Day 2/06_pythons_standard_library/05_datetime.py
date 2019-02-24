from datetime import date, datetime, timedelta


# Date only
date_object = date.today()
print("Current date:", date_object)

# Date & time
datetime_object = datetime.today()
print("Current date/time:", datetime_object)
print("Year:", date_object.year)
print("Month:", date_object.month)
print("Day:", date_object.day)


# Get a date in the future or past:
one_week_and_three_days_ago = datetime.today() - timedelta(weeks=1, days=3)

print("Date/Time one week and three days ago:", one_week_and_three_days_ago)
