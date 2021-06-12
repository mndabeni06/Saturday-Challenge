from datetime import date, timedelta

dob = date(1999, 1, 20)
age = (date.today() - dob)//timedelta(days=365.245)
print(age)
