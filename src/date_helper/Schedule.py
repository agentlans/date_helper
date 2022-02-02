from datetime import date, timedelta
from BusinessDays import start_of_week

def start_of_month(year, month):
  "Returns the first day of the month."
  return date(year, month, 1)

def days(n):
  '''Returns an object representing n days 
  that can be added or subtracted to dates.'''
  return timedelta(days=n)

def end_of_month(year, month):
  "Returns the last day of the month."
  # Go to next month and subtract one day
  if month == 12:
    year += 1
    month = 1
  else:
    month += 1
  return start_of_month(year, month) - days(1)

# print(end_of_month(2022, 11))

def nth_xday(year, month, n, day_of_week):
  '''Returns the nth {Mon,Tue,Wed,...}day of the month.
  Monday is 0, Sunday is 6.
  '''
  som = start_of_month(year, month)
  sow = start_of_week(som)
  if day_of_week < som.weekday():
    return sow + days(7 * n) + days(day_of_week)
  else:
    return sow + days(7 * (n-1)) + days(day_of_week)

def nth_last_xday(year, month, n, day_of_week):
  '''Returns the nth last {Mon,Tues,...}day of the month.
  Monday is 0, Sunday is 6.'''
  eom = end_of_month(year, month)
  sow = start_of_week(eom)
  if day_of_week < eom.weekday():
    return sow - days(7 * (n-1)) + days(day_of_week)
  else:
    return sow - days(7 * n) + days(day_of_week)

# 3rd Friday (day_of_week = 4) of Jan. 2022
# print(nth_xday(2022, 1, 3, 4)) # 2022-01-21
# 3rd last Friday of Jan. 2022
# print(nth_last_xday(2022, 1, 3, 4)) # 2022-01-14
