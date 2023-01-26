# Modules:
import modul1 as m      # modul1.function() and as m is sort_name
from modul1 import *    # all function used
print (m.sum1(10,20))   # 30
print (m.multi1(10,20)) # 200

# direct modual function call
print(sum1(20,30))        
print(multi1(2,3))

# modul1.py python files create
# def sum1(a,b):
#     c = a+b
#     return c
# def multi1(a,b):
#     c = a*b
#     return c
x = [10,20,30]
import math
print(math.ceil(12.8))      # 13
print(math.floor(12.8))     # 12
print(math.fabs(-10))       # 10.0 
print(math.factorial(5))    # 120
print(math.fsum(x))         # 60.0
print(math.sqrt(16))        # 4.0

# Random Moduals:
import random
print(random.randint(5,10))     # random 5 to 10
print(random.randrange(5,10))   # random 5 to 9
i = ['apple', 'ball', "cat"]    
print(random.choice(i))         # random choise

r = random.random()
print(r)    # 0 t0 1 no, print in float

random.shuffle(i)
print(i)    # change list suffle use

r = random.uniform(3,8)
print(r)    # random 3 to 8 but float no.

# Data Time Modual:
import datetime
x = datetime.datetime.now()
print(x)  # 2022-12-21 13:52:58.256006

print(datetime.datetime(2022,2,22))  # 2022-02-22 00:00:00

now = datetime.datetime.now()
year = now.strftime("%Y")
print('year',year)      # year 2022

# Directive	Meaning	                                        Output Format
# %a	Abbreviated weekday name.	                            Sun, Mon, …
# %A	Full weekday name.	                                    Sunday, Monday, …
# %w	Weekday as a decimal number.	                        0, 1, …, 6
# %d	Day of the month as a zero added decimal.	            01, 02, …, 31
# %-d	Day of the month as a decimal number.	                1, 2, …, 30
# %b	Abbreviated month name.	                                Jan, Feb, …, Dec
# %B	Full month name.	                                    January, February, …
# %m	Month as a zero added decimal number.	                01, 02, …, 12
# %-m	Month as a decimal number.	                            1, 2, …, 12
# %y	Year without century as a zero added decimal number.	00, 01, …, 99
# %-y	Year without century as a decimal number.	            0, 1, …, 99
# %Y	Year with century as a decimal number.	                2013, 2019 etc.
# %H	Hour (24-hour clock) as a zero added decimal number.	00, 01, …, 23
# %-H	Hour (24-hour clock) as a decimal number.	            0, 1, …, 23
# %I	Hour (12-hour clock) as a zero added decimal number.	01, 02, …, 12
# %-I	Hour (12-hour clock) as a decimal number.	            1, 2, … 12
# %p	Locale’s AM or PM.	                                    AM, PM
# %M	Minute as a zero added decimal number.	                00, 01, …, 59
# %-M	Minute as a decimal number.	                            0, 1, …, 59
# %S	Second as a zero added decimal number.	                00, 01, …, 59
# %-S	Second as a decimal number.	                            0, 1, …, 59
# %f	Microsecond as a decimal no., zero added on the left.	000000 – 999999
# %z	UTC offset in the form +HHMM or -HHMM.	 
# %Z	Time zone name.	 
# %j	Day of the year as a zero added decimal number.	        001, 002, …, 366
# %-j	Day of the year as a decimal number.	                1, 2, …, 366
# %U	Week number of the year 	                            00, 01, …, 53
# %W	Week number of the year 	                            00, 01, …, 53

