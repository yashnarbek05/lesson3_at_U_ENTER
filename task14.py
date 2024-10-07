from calendar import Calendar, calendar, TextCalendar
from datetime import datetime, date
from sqlite3 import Date
from xmlrpc.client import DateTime

date1 = input("Enter first date(year,month,day): ").split('.')
date2 = input("Enter second date(year,month,day): ").split('.')

date11 = Date(int(date1[0]),int(date1[1]),int(date1[2]))
date12 = Date(int(date2[0]),int(date2[1]),int(date2[2]))


print(date12 - date11)