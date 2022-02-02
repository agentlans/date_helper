# date-helper

Small utilities for handling business day and time zone calculations.

# Install, Use
1. Clone this repository
2. (Optional) To build the wheels, run `python -m build` from the current directory
3. Run `pip install . --use-feature=in-tree-build` from the current directory
4. Use the package from Python code

```python
import date_helper
from date_helper.TimeZones import *
from date_helper.BusinessDays import *

# Find current time in Sydney, Australia
convert_time_zone(now_local(), "Australia/Sydney")

# Number of Canadian business days from Jan. 1, 2022 to Jan. 1, 2023
business_days_between(date(2022, 1, 1), date(2023, 1, 1), holidays.CA())
```

# Author, License

Copyright :copyright: 2022 Alan Tseng

MIT License
