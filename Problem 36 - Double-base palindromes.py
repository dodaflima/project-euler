#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

is_palindrome = lambda x: x == x[::-1]
to_bin_number = lambda x: str(bin(x))[2:]
numbers_sum = 0

for i in range(1, 1000001):
    if is_palindrome(str(i)) and is_palindrome(to_bin_number(i)):
        numbers_sum += i

# Answer
print(numbers_sum)