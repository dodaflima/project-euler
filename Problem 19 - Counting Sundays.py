#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import date

def first_day_on_monday_since_before(initial_year, end_year):
    number_of_days = 0

    for year in range(initial_year, end_year+1):
        for month in range(1, 13):
            day = date(year, month, 1)

            if day.weekday() == 6:
                number_of_days += 1

    return number_of_days

# Answer
print(first_day_on_monday_since_before(1901, 2000))
