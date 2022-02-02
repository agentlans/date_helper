from datetime import date, timedelta
import holidays

def start_of_week(dt):
  "Returns the Monday of the week containing the date dt."
  return dt - timedelta(days=dt.weekday())

def weekdays_since_start_of_week(dt):
  return min(dt.weekday(), 5) # 5 is Sat., 6 is Sun.

def weekdays_between(d1, d2):
  "Returns number of weekdays in [d1, d2)."
  a = (start_of_week(d2) - start_of_week(d1)) / 7
  return a.days * 5 + \
    weekdays_since_start_of_week(d2) - \
    weekdays_since_start_of_week(d1)

# weekdays_between(date(2022, 1, 30), date(2022, 2, 3))

def is_weekday(d):
  return d.weekday() < 5

def sort_dates(d1, d2):
  if d1 < d2:
    return d1, d2
  else:
    return d2, d1

def weekday_holidays_between(dt1, dt2, holiday_obj):
  "Number of holidays that occur on weekdays in [d1, d2)."
  d1, d2 = sort_dates(dt1, dt2)
  # Look up the dates so holiday_obj will generate list of holidays in range
  d = d1
  while d <= d2:
    d in holiday_obj
    d += timedelta(days=365)
  d in holiday_obj
  return len([h for h in holiday_obj if d1 <= h and h < d2 and is_weekday(h)])

def business_days_between(d1, d2, holiday_obj):
  "Number of days in [d1, d2) that aren't weekends or holidays."
  sign = 1
  if d1 > d2:
    sign = -1 # reverse the sign if necessary
  return sign * (abs(weekdays_between(d1, d2)) - \
    weekday_holidays_between(d1, d2, holiday_obj))

def is_business_day(d, holiday_obj):
  "Returns True iff d isn't a holiday or on a weekend."
  return is_weekday(d) and (not d in holiday_obj)

def previous_business_day(d, holiday_obj, n=1):
  "Returns the nth business day before date d."
  d2 = d
  num_found = 0
  while num_found < n:
    d2 -= timedelta(days=1)
    if is_business_day(d2, holiday_obj):
      num_found += 1
  return d2

def next_business_day(d, holiday_obj, n=1):
  "Returns the nth business day after date d."
  d2 = d
  num_found = 0
  while num_found < n:
    d2 += timedelta(days=1)
    if is_business_day(d2, holiday_obj):
      num_found += 1
  return d2

# Number of business days in 2022 in Canada
# x = business_days_between(date(2022, 1, 1), date(2023, 1, 1), holidays.CA())
# print(x) # 250 days
# https://www.timeanddate.com/date/workdays.html says 252 days
#   but doesn't include Easter Monday and Civic Holiday

# Note: these routines only work with dates, not datetimes.
# For example, this doesn't work:
# from datetime import datetime
# business_days_between(datetime(2022, 1, 1, 10, 0, 0), \
#  datetime(2023, 1, 1, 3, 0, 0), holidays.CA())

# print(next_business_day(date(2022, 1, 1), holidays.CA(), 250))
