import time
import calendar
import datetime
birthday = datetime.date(1986, 9, 5)
print("my birthday is:", birthday)
print("the birthday year is:", birthday.year)
print("the birthday month is:", birthday.month)
print("the birthday day is:", birthday.day)
print("the birthday in week day:", birthday.isoweekday())
btd = datetime.date(2019, 9, 5 )
today = datetime.date.today()
till_bd = btd - today
print (till_bd)

cal = calendar.month(2017, 5)
print (cal)
current_time = time.asctime()
print(current_time)

yesterday_time = datetime.date(2019, 9,1)
tdelta = datetime.timedelta(days =2)
tdelta1 = datetime.timedelta(days=3)
print("plus 2 days:", yesterday_time + tdelta)
print("minus 3 days:", yesterday_time - tdelta1)
