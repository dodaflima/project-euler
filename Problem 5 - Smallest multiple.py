#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

2520 é o menor número que pode ser dividido por cada um números entre 1 e 10 sem resto.
Qual é o menor número positivo que é divisivel por todos os números entre 1 e 20?
"""

from math import prod

number_list = [x+1 for x in range(20)]

# Function to find prime numbers
def find_primes_until(number):
    primes = [2]
    init = 2

    while init <= number:
        tries = []
        
        if init == 2:
            yield init
            init += 1
            continue

        for prime in primes:
            if init % prime == 0:
                tries.clear()
                break
            else:
                tries.append(True)

        if len(tries) == len(primes):
            primes.append(init)
            init += 1
            yield primes[-1]

        else:
            init += 1

def get_divisors_number(number_list: list[int]) -> list[int]:
    primes_until_max = max(number_list) + 1 
    primes_list = list(find_primes_until(primes_until_max))
    has_remainder = lambda number, div: number % div != 0
    remove_number_one = lambda array: [x for x in array if x != 1]

    while len(primes_list) != 0:
        remove_number_one(number_list)
        can_add = False
        can_pop_prime = []

        if len(primes_list) > 0:
            prime = primes_list[0]

        for index, value in enumerate(number_list):
            if not has_remainder(value, prime):
                number_list[index] = value / prime
                can_add = True
                
            else:
                can_pop_prime.append(True)

        if len(can_pop_prime) == len(number_list):
            primes_list.pop(0)

        if can_add:
            yield prime


# Answer
numbers = list(get_divisors_number(number_list))
print(prod(numbers))
