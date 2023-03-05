#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
n! means n x (n - 1) x ... x 3 x 2 x 1
For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!

n! significa n x (n - 1) x ... x 3 x 2 x 1
Por exemplo, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
e a soma dos digitos do número é 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Encontre a soma dos digitos do número 100!
'''

from math import prod

def fat(number):
    number = abs(number)
    numbers = []
    while number > 0:
        numbers.append(number)
        number -= 1
    return prod(numbers)

digits_sum = lambda number: sum([int(x) for x in str(fat(number))])

# Answer
print(digits_sum(100))