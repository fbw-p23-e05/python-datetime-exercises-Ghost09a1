from datetime import datetime, timedelta
current_datetime = datetime.now()

# Print 
print("Today:", current_datetime)

# next 5 days
for i in range(1, 6):
    next_day = current_datetime + timedelta(days=i)
    print(next_day.strftime("%Y-%m-%d %H:%M:%S.%f"))

