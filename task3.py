from datetime import datetime, timedelta
current_time = datetime.now().time()

current_datetime = datetime.combine(datetime.today(), current_time)

new_datetime = current_datetime + timedelta(seconds=5)

# print 
print("Current time:", current_datetime.strftime("%H:%M:%S.%f"))
print("After adding 5 seconds:", new_datetime.strftime("%H:%M:%S.%f"))
