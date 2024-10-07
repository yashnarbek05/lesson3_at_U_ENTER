from calendar import TextCalendar

year = int(input("Year: "))
month = int(input("Month: "))

cal = TextCalendar().formatmonth(year, month)

print(cal)