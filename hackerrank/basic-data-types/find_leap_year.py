#Task

#Given a year, determine whether it is a leap year. If it is a leap year,
#return the Boolean True, otherwise return False.

#Input format

#Read "year" the year to test.

#Constraints
# 1900 <= year <= 10^5

#Output format

#The function must return a Boolean value (True/False).

from math import *

def is_leap(year):
    leap = False

    if year < 1900 or year > pow(10, 5):
        year = int(input())
    elif year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap


year = int(input())

