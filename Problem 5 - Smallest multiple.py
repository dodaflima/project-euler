#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

2520 é o menor número que pode ser dividido por cada um números entre 1 e 10 sem resto.
Qual é o menor número positivo que é divisivel por todos os números entre 1 e 20?
"""

from math import prod

# Function to find prime numbers
def find_primes_until(number):
    primes = [2]
    init = 2

    while init <= number:
        tries = []

        if init == 2:
            init += 1
            continue

        for prime in primes:
            if init % prime == 0:
                tries.clear()
                break
            else:
                tries.append(False)
        if not any(tries) and len(tries) == len(primes):
            primes.append(init)
        init += 1

    return primes

has_remainder = lambda number, div: number % div != 0
remove_number_one = lambda array: [x for x in array if x != 1]
number_list = [x+1 for x in range(20)]
primes_until_max = find_primes_until(20)
prod_list = []

while len(primes_until_max) != 0:
    remove_number_one(number_list)
    can_add = False

    if len(primes_until_max) > 0:
        prime = primes_until_max[0]
        
    for index, value in enumerate(number_list):
        if not has_remainder(value, prime):
            number_list[index] = value / prime
            can_add = True

    if can_add:
        prod_list.append(prime)

    if number_list.count(primes_until_max[0]) == 0:
        primes_until_max.pop(0)

# Answer
print(prod(prod_list))