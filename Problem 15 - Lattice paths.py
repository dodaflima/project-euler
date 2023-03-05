#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?

Começando do canto superior esquerdo em uma grade 2x2,
e somente sendo capaz de se mover para direita e para baixo,
há exatamente 6 caminhos para o canto inferior direito.
Quantos caminhos possiveis há em uma grade 20x20?
'''

from math import prod

def fat(number):
    number = abs(number)
    numbers = []
    while number > 0:
        numbers.append(number)
        number -= 1
    return prod(numbers)

answer = lambda x, y: int(fat(x+y) / (fat(x) * fat(y)))

# Answer
print(answer(20, 20))