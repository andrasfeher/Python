# leap year
import calendar
print(calendar.isleap(1900))
print(calendar.isleap(1996))

# datetime module
from datetime import date

myBirthday = date(1967, 2, 1)
print(myBirthday)
print(myBirthday.day)
print(myBirthday.month)
print(myBirthday.year)
print(myBirthday.isoformat())


# date delta
from datetime import timedelta

now = date.today()
one_day = timedelta(days = 1)

tomorrow = now + one_day
print(tomorrow)

print(now + 17 * one_day)

yesterday = now - one_day
print(yesterday)

# datetime
from datetime import datetime
now = datetime.now()
print(now)
print(now.isoformat())
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.second)
print(now.microsecond)


# unixtime, localtime, gmtime
import time
now = time.time()
print(now)
print(time.localtime(now))
print(time.gmtime(now))


# formatted time
# %Y year 1900-…
# %m month 01-12
# %B month name January, …
# %b month abbrev Jan, …
# %d day of month 01-31
# %A weekday name Sunday, …
# a weekday abbrev Sun, …
# %H hour (24 hr) 00-23
# %I hour (12 hr) 01-12
# %p AM/PM AM, PM
# %M minute 00-59
# %S second 00-59

import time
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(time.strftime(fmt, t))

# convert string to time
import time

fmt = "%Y-%m-%d"
print(time.strptime("2012-01-28", fmt))
