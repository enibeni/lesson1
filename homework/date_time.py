from datetime import datetime, timedelta, date, time

# вчера сегодня, месяц назад

now = datetime.now()
delta_day = timedelta(days=1)
delta_month = timedelta(365/12)


print("Today: " + now.strftime('%d.%m.%Y'))
yesterday = now - delta_day
print("Yesterday: " + yesterday.strftime('%d.%m.%Y'))
month_later = now + delta_month
print("One month later: " + month_later.strftime('%d.%m.%Y'))

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)

end = time(18, 30, 0, 0)
now = datetime.now().time()
when = datetime.combine(date.today(), end) - datetime.combine(date.today(), now)
print(when)
