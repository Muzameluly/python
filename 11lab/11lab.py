from math import *

#math модуль
iterable = [10,2,5]

x=prod(iterable)
print(x)

y=prod(iterable,start=2)
print(y)

print("------------------------")

speed=10 #метр/сек
distance_moved=-3 #метр
velosity=copysign(speed,distance_moved)
print(velosity)

print("------------------------")

n=10
k=6
x=comb(n,k) #n!/(k1!*(n-k)!)
print(x)
y=perm(n,k) #n!/(n-k)!
print(y)

print("------------------------")

x=ceil(4.333)
print(x)

y=floor(3.652)
print(y)

print("------------------------")

#random модуль

import random

mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))
print(random.choices(mylist, weights = [10, 1, 1], k = 14))

print("------------------------")

print(random.uniform(20, 60))
print(random.triangular(20, 60, 30))

print("------------------------")

print(random.random())

state = random.getstate()

print(random.random())

random.setstate(state)

print(random.random())

print("------------------------")

#datetime модуль
import datetime
from datetime import date,time,timedelta
import pytz

datetime_object = datetime.datetime.now()
print(datetime_object)
print("Year: ", datetime_object.year)
print("Month: ", datetime_object.month)
print("Date: ", datetime_object.day)
print("Hour: ", datetime_object.hour)
print("Minute: ", datetime_object.minute)
print("Second: ", datetime_object.second)

print("------------------------")


today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

print("------------------------")

a = time(14,15,25)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)


print("------------------------")

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)

print("------------------------")

local = datetime.datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))


tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

print("------------------------")




