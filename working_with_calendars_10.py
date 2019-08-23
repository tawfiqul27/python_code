# Working with calenders
#


# import the calender module
import calendar



# create a plan text calender
c = calendar.TextCalendar(calendar.SUNDAY)
pt = c.formatmonth(2017, 1, 0, 0)
print(pt)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2017, 1)
print(st)


# loop over the days of a month
# zeros mean that the day of week is in an overlapping month
for i in c.itermonthdays(2017, 8):
    print(i)            # there will be zeros at the begining and ending of the output which indicates that there are days on that weeks



# The calendar module provides useful utilities for the given locale, such as the name of days
# and months in both full and abbreviated forms

for name in calendar.month_name:
    print(name)


for day in calendar.day_name:
    print(day)


# Calculate days based on a rule: For example, consider a team meeting on the first Friday of every month.
# To figure out what days that would be for each month, we can use this script:

print("Team meetings will be on: ")
for m in range(1,13):
    cal = calendar.monthcalendar(2018, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    
    print("%10s %2d" % (calendar.month_name[m], meetday))


