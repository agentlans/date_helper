# Description of date_helper modules

## date_helper.BusinessDays

- The variables `d, d1, d2` refer to `datetime.date` Python objects.
- Intervals between dates are half-open intervals `[d1, d2)` which include `d1` but not `d2`.
- `holiday_obj` is a holiday object from the [holidays package](https://pypi.org/project/holidays/)
- Weekends are assumed to be the Saturday and Sunday of every week.

```python
weekdays_between(d1, d2)
business_days_between(d1, d2, holiday_obj)
# Returns the number of weekdays and business days in [d1, d2), respectively.

is_business_day(d, holiday_obj)
# Returns True if d isn't a weekend or a holiday

previous_business_day(d, holiday_obj, n=1)
next_business_day(d, holiday_obj, n=1)
# Returns the nth business day before or after date d, respectively.
```

## date_helper.Schedule

- Months are specified as integers where January is 1 and December is 12.
- Days of the week are specified as integers where Monday is 0 and Sunday is 6

```python
start_of_month(year, month)
end_of_month(year, month)
# Returns the first or the last day of the month, respectively

nth_xday(year, month, n, day_of_week)
nth_last_xday(year, month, n, day_of_week)
# Returns the nth {Mon,Tues,Wed,...} of the month where n >= 1.
# nth_last_xday counts the nth day backwards 
# starting from the end of the month.
```

## date_helper.TimeZones
- Times refer to time zone-aware `datetime.datetime` objects
- Time zones are `ZoneInfo` objects
- The functions below can also accept strings as time zones (for example, "Pacific/Honolulu")

```python
current_time_zone()
# Returns the time zone as given by the computer's settings.

make_date(year, month, day, hour=0, minute=0, second=0, 
  tzinfo=current_time_zone())
# Returns a datetime object with the given time zone.

now_local()
now_utc()
# Returns the current time as a time zone-aware datetime in either the local or UTC time zones.

convert_time_zone(dt, new_time_zone)
# Expresses and returns the datetime dt as a local time in another time zone.
```
