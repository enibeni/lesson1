import datetime
import ephem

now = datetime.datetime.now()
date = str(now.year) + '/' + str(now.month) + '/' + str(now.day)
print(ephem.next_full_moon(date))
