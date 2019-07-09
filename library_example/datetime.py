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

d1 = datetime.date(2019, 7, 8)
print(d1)
# 2019-07-08

#d1 = datetime.date(2019, 13, 8)
# ValueError                                Traceback (most recent call last)
#<ipython-input-8-a38be9935a92> in <module>()
#----> 1 d1 = datetime.date(2019, 13, 8)
# ValueError: month must be in 1..12