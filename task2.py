from datetime import datetime, timedelta
current_date = datetime.now()# current date
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

# Print 
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", current_date.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))
