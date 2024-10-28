import datetime

Y = int(input())
october = datetime.datetime(Y, 10, 31)
while october.weekday() != 5:  # 5 represents Saturday
    october -= datetime.timedelta(days=1)
print(october.day)