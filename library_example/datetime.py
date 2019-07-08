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