import random
import math
import datetime
import calendar
import os
import antigravity
courses=['Math','Art','Science','History','Geography']
print(random.choice(courses))

deg=input('Enter Degree: ')
rads=math.radians(float(deg))
print(rads)
print(math.sin(rads))


today=datetime.date.today()
print(today)


print(calendar.isleap(2020))
print(os.getcwd())
print(os.__file__)
# print(os.__doc__)
# print(os.__name__)
# print(os.__package__)
# print(os.__loader__)
# print(os.__spec__)

print(antigravity.__file__)