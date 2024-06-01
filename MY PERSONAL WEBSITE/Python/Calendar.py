import calendar
year = eval(input("Year: "))
month = eval(input("Month: "))
if year and month > 0:
    print(calendar.month(year, month))
else:
    print("Invalid Input, Please try again.")
