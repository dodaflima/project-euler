#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Um terno pitagórico é um conjunto de três números naturais, a < b < c, para o qual
a² + b² = c²
Por exemplo, 3² + 4² = 9 + 16 = 25 = 5².
Existe exatamente UM terno pitagórico para o qual a + b + c = 1000.
Encontre o produto abc
"""

from math import prod

pythagorean_list = [(3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17), (9, 40, 41), (11, 60, 61), (12, 35, 37), (13, 84, 85), (16, 63, 65), (20, 21, 29)]
possible = [x+1 for x  in range(100)]

answer = []

for triplet in pythagorean_list:
    for p in possible:
        x = p * triplet[0]
        y = p * triplet[1]
        z = p * triplet[2]
        soma = sum([x, y, z])
        
        if soma == 1000:
            answer = [x, y, z]
            break
        if soma > 1000:
            break
    if len(answer) != 0:
        break

# Answer (Or error)
print(f"(x, y , z): {answer[0]}, {answer[1]}, {answer[2]}, soma: {prod(answer)}")