import date_helper
from date_helper.TimeZones import *
from datetime import date, timedelta

# These functions only work on datetime objects with date and time components.
# Start of the week is Monday 00:00 in the datetime's time zone.

# Time units (attributes of datetime objects) in descending order
time_units = ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']

def minimum(time_unit):
  "Minimum legal value of each time unit"
  if time_unit == 'year':
    return datetime.MINYEAR
  elif time_unit == 'month':
    return 1
  elif time_unit == 'day':
    return 1
  else:
    return 0

def week_frac(dat):
  "The time since the start of the week which is Monday"
  return timedelta(days=dat.weekday(), 
    hours=dat.hour, minutes=dat.minute, seconds=dat.second, 
    microseconds=dat.microsecond)

def week_floor(dat):
  return dat - week_frac(dat)

def week_ceil(dat):
  if week_frac(dat) == timedelta():
    return week_floor(dat)
  else:
    return week_floor(dat) + timedelta(days=7)

def make_datetime(parts, tzinfo):
  "Returns a datetime from a list of its parts."
  return datetime(parts[0], parts[1], parts[2],
    parts[3], parts[4], parts[5], parts[6], tzinfo=tzinfo)

def date_floor(dt, time_unit):
  "The datetime rounded down to time_unit."
  assert time_unit in time_units + ['week']
  if time_unit == 'week':
    return week_floor(dt)
  # Go through each part
  parts = []
  set_min = False
  for tp in time_units:
    if set_min:
      parts.append(minimum(tp))
    else:
      parts.append(getattr(dt, tp))
    # Minimize every part after this part
    if tp == time_unit:
      set_min = True
  # Create a date from those parts
  return make_datetime(parts, dt.tzinfo)

def date_frac(dt, time_unit):
  """The fractional part of the datetime rounded down to time_unit.
  Returns a timedelta object.
  """
  return dt - date_floor(dt, time_unit)

def date_ceil(dt, time_unit):
  "The datetime rounded up to time_unit."
  assert time_unit in time_units + ['week']
  if time_unit == 'week':
    return week_ceil(dt)
  # Check if it's exactly a multiple of time_unit
  if date_frac(dt, time_unit) == timedelta():
    return date_floor(dt, time_unit)
  else:
    parts = []
    # Go through each part
    set_min = False
    for tp in time_units:
      if tp == time_unit:
        # time_unit + 1
        parts.append(getattr(dt, tp) + 1)
        # Set everything to the right of tp to their minimum values
        set_min = True
      elif set_min:
        parts.append(minimum(tp))
      else:
        # The same time_unit unchanged
        parts.append(getattr(dt, tp))
    return make_datetime(parts, dt.tzinfo)

def date_linspace(start, stop, num, endpoint=True):
  """List of num evenly-spaced time points in [start, stop].
  If endpoint = False, then the interval [start, stop)."""
  n = 0
  if endpoint:
    # num fenceposts. Need to get num-1 equally-spaced numbers.
    n = num - 1
  else:
    n = num
  delta = (stop - start) / n
  return [start + i * delta for i in range(num)]

