#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million

A soma dos números primos abaixo de 10 são 2 + 3 + 5 + 7 = 17
Encontre a soma de todos os números primos abaixo de dois milhões
"""

def find_primes_until(number):
    primes = [2]
    init = 3

    while init <= number:
        tries = []

        for prime in primes:
            if init % prime == 0:
                tries.clear()
                break
            else:
                tries.append(False)
        if not any(tries) and len(tries) == len(primes):
            primes.append(init)
        init += 2

    return primes
    
number = find_primes_until(2000000)

print(sum(number))