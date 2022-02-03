# date_helper

Utilities for business day and time zone calculations.

# Install and use
1. Clone this repository
2. (Optional) To build the wheels, run `python -m build` from the current directory
3. (Optional) Create a virtual environment (venv or conda)
4. Run `pip install . --use-feature=in-tree-build` from the current directory
5. Use the package from Python code. For example,

```python
import date_helper
from date_helper.TimeZones import *
from date_helper.BusinessDays import *

# Find current time in Sydney, Australia
convert_time_zone(now_local(), "Australia/Sydney")

# Number of Canadian business days from Jan. 1, 2022 to Jan. 1, 2023
business_days_between(date(2022, 1, 1), date(2023, 1, 1), holidays.CA())
```

For more details, see the included [documentation](doc.md).

# Author and license

Copyright :copyright: 2022 Alan Tseng

MIT License
