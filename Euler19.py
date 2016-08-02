import datetime

def countingSundays(startDate, endDate):
    ans = 0
    while startDate != endDate:
        if(startDate.day == 1 and startDate.weekday() == 6):
            # print(str(startDate.year) + ", " + str(startDate.month))
            ans += 1
        startDate = startDate + datetime.timedelta(1)
    return ans

print(countingSundays(datetime.date(1901, 1, 1), datetime.date(2000, 12, 31)))
