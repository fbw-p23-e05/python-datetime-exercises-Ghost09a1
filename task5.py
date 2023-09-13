from datetime import datetime

# Year/Month/Day
year = 2023
month = 3
day = 12

date_to_convert = datetime(year, month, day)

day_of_year = date_to_convert.strftime("%j")

# Print 
print("Today:", date_to_convert)
print("Day of the year:", day_of_year)
