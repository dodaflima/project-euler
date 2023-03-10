#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

A seguinte sequência interativa é definida por um conjunto de números positivos:
n → n/2 (se n for par)
n → 3n + 1 (se n for impar
Usando a regra acima começando com 13, geramos a sequência abaixo)
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
É possível observar que essa sequência (começando com 13 e terminando com 1), contém 10 termos.
Apesar de ainda não ser provado (Problema de Collatz), pensasse que todos os números iniciais acabam em 1.
Qual número inicial, abaixo de um milhão, produz a maior sequência?
NOTA: Uma vez que a sequência inicie os termos podem ser maiores que um milhão
"""

is_even = lambda x: x % 2 == 0
if_even = lambda x: int(x / 2)
if_odd = lambda x: int((3 * x) + 1)

def collatz(n):
    while n > 1:
        if is_even(n):
            n = if_even(n)
            yield n
        else:
            n = if_odd(n)
            yield n

def answer(number_try):
    answer_number = 0
    answer_number_list = []
    try_number_list = []

    while number_try > 1:

        for i in collatz(number_try):
            try_number_list.append(i)

        if len(try_number_list) > len(answer_number_list):
            answer_number = number_try
            answer_number_list = try_number_list.copy()

        try_number_list.clear()
        number_try -= 1

    return answer_number

# Answer
print(answer(1000000))