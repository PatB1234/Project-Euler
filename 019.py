import datetime
first = datetime.date(1901, 1, 1)
last = datetime.date(2000, 12, 31)
curr_day = first
nSundays = 0
while curr_day < last:

    if curr_day.weekday() == 6 and curr_day.day == 1: # Returns the day of the week and the current day of the month

        nSundays += 1

    curr_day += datetime.timedelta(days=1)
    

print(nSundays)