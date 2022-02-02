from zoneinfo import ZoneInfo # Note: must pip install tzdata
from datetime import datetime, timedelta, timezone

def current_time_zone():
  "Returns the current time zone of the computer as a timezone object."
  return datetime.now().astimezone().tzinfo

def now_utc():
  "Returns the current time as a time zone-aware object in UTC."
  return datetime.now(timezone.utc)

def now_local():
  "Returns the current time in the current time zone as a time zone-aware object."
  return datetime.now().astimezone()

def lookup(obj):
  if type(obj) == str:
    return ZoneInfo(obj)
  else:
    return obj

def make_date(year, month, day, hour=0, minute=0, second=0, 
  tzinfo=current_time_zone()):
  "Returns a datetime in the given time zone."
  return datetime(year, month, day, hour, minute, second, tzinfo=lookup(tzinfo))

def convert_time_zone(dt, new_time_zone):
  "Returns the given time in another time zone."
  return dt.astimezone(lookup(new_time_zone))
