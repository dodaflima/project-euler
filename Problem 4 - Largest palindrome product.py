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

def get_largest_palin_between(first_num_size_limit: int, second_num_size_limit: int) -> int:

    palindrome: int = 0
    first_number: int = 0
    second_number: int = 0
    check_is_palindrome: bool = lambda x: True if str(x)[::-1] == str(x) else False

    while first_number <= first_num_size_limit:

        while second_number <= second_num_size_limit:

            palin = first_number * second_number

            cond_one: bool = check_is_palindrome(palin)
            cond_two: bool = palin > palindrome

            if cond_one and cond_two:
                palindrome = palin

            second_number += 1

        first_number += 1
        second_number = 0

    return palindrome

# Get the result
answer: int = get_largest_palin_between(1000, 1000)
print(answer)
