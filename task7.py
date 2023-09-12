from datetime import datetime, timedelta

# Input:
year = int(input("Input a year: "))

first_day_of_year = datetime(year, 1, 1)

one_day = timedelta(days=1)

sundays = []

current_date = first_day_of_year
while current_date.year == year:
    if current_date.weekday() == 6:  # (0 = Sunday)
        sundays.append(current_date.strftime('%Y-%m-%d'))
    current_date += one_day

# Print 
for i, sunday in enumerate(sundays):
    if i % 7 == 0 and i != 0:
        print('-' * 10)
    print(sunday)
