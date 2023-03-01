#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Um número palíndromo é lido nas duas direções
O maior palíndromo obtido com o produto de dois número de 2 dígitos é 9009 = 91 x 99
Encontre o maior palíndromo feito a partir do produto de dois números de 3 dígitos
"""

check_is_palindrome = lambda x: True if str(x)[::-1] == str(x) else False

def get_largest_palin_between(x: int, y: int) -> int:
    palindrome: int = 0
    a = 4
    b = 4
    while a < x:
        while b < y:
            palin = a * b
            if check_is_palindrome(palin) \
                and len(str(a)) == 3 \
                and len(str(b)) == 3 \
                and palin > palindrome:

                palindrome = palin
            b += 1
        a += 1
        b = 4
    return palindrome

# Get the result
answer = get_largest_palin_between(1000, 1000)
print(answer)