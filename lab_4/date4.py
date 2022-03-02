from datetime import datetime, timedelta, time
x = datetime.now()
y = datetime.strptime("2 March 2020, 09:00:00", "%d %B %Y, %H:%M:%S")
z = (x - y).seconds
print(z)

