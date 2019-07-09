import datetime

t1 = datetime.timedelta(hours=3)
t2 = datetime.timedelta(hours=2)
t3 = t1+t2
print(t3)
# 5:00:00
t4 = t1-t2
print(t4)
print(+t4)
print(-t4)
# 1:00:00
# 1:00:00
# -1 day, 23:00:00

year = datetime.timedelta(days=365)   # 365 days
another_year = datetime.timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600) # another 365 days
print(another_year.total_seconds())   # 31536000.0