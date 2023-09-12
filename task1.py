from datetime import datetime, timedelta

current_datetime = datetime.now()
print("Current date and time:", current_datetime)
print("Current year:", current_datetime.year)
print("Month of year:", current_datetime.strftime('%B'))
print("Week number of the year:", current_datetime.strftime('%U'))
print("Weekday of the week:", current_datetime.strftime('%A'))
print("Day of year:", current_datetime.strftime('%j'))
print("Day of the month:", current_datetime.day)
print("Day of week:", current_datetime.strftime('%A'))
print()
