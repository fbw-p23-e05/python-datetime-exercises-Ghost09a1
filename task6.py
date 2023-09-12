from datetime import datetime, timedelta

# Input: 
year = 2023
week_number = 11
first_day_of_week = datetime.fromisocalendar(year, week_number, 1)


while first_day_of_week.weekday() != 0:  # 0 represents Monday
    first_day_of_week += timedelta(days=1)

# Print 
print("The first Monday of this week was:", first_day_of_week.strftime('%Y-%m-%d'))
