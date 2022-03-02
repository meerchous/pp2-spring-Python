import datetime
from turtle import end_fill
x = datetime.datetime.now()
yesterday = x+datetime.timedelta(days=-1)
tommorow = x+datetime.timedelta(days=+1)
print(str(yesterday)+"\n"+str(x)+"\n"+str(tommorow))