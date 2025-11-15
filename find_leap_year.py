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