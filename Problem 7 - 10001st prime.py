#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

Listando os seis primeiros números primos: 2, 3, 5, 7, 11 e 13, podemos ver que o 6° número primo é o 13.
Qual é p 10001° número primo?
"""

def find_primes(number):
    primes = [2]
    init = 2

    while len(primes) != number:
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
                tries.append(False)
                
        if len(tries) == len(primes):
            primes.append(init)
            init += 1
            yield primes[-1]

        else:
            init += 1

the_primes = find_primes(10001)

# Answer
print(list(the_primes)[-1])
