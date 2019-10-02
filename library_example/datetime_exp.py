import datetime
import pytz
from pytz import timezone

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

t = datetime(2009, 7, 10, 18, 44, 59, 193982, tzinfo=pytz.utc)
print(str(t))
# 2009-07-10 18:44:59.193982+00:00

local_tz = pytz.timezone('Europe/Moscow')
t = datetime(2009, 7, 10, 18, 44, 59, 193982, tzinfo=local_tz)
print(str(t))
# 2009-07-10 18:44:59.193982+02:30

now_time = datetime.datetime.utcnow()
print(now_time)
now_time.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
# datetime change utc timezone to local timezone
# 2019-07-11 02:28:21.656157
# datetime.datetime(2019, 7, 10, 22, 28, 21, 656157, tzinfo=datetime.timezone(datetime.timedelta(-1, 72000), 'Eastern Summer Time'))

now_time.tzinfo
tzchina = timezone('Asia/Chongqing')
tzchina
utc = timezone('UTC')
now_time.replace(tzinfo=utc).astimezone(tzchina)
# using pytz to change timezone
# datetime.datetime(2019, 7, 11, 10, 28, 21, 656157, tzinfo=<DstTzInfo 'Asia/Chongqing' CST+8:00:00 STD>)

from pytz import timezone
tzchina.utcoffset(datetime.datetime.now())
tzfr = timezone('Europe/Paris')
utc = timezone('UTC')
print(now_time.replace(tzinfo=utc).astimezone(tzfr))
tzfr.utcoffset(datetime.datetime.now())
# 2019-07-12 02:47:27.296258+02:00
# datetime.timedelta(0, 7200)

d = datetime.date.fromordinal(730920) # 730920th day after 1. 1. 0001
d # datetime.date(2002, 3, 11)

t = d.timetuple()
for i in t:
    print(i)
# 2002    # year
# 3       # month
# 11      # day
# 0
# 0
# 0
# 0       # weekday (0 = Monday)
# 70      # 70th day of year
# -1
d.strftime("%Y-%m-%d")
# "2002-03-11'
d.strftime("%Y-%B-%a")
# '2002-March-Mon'