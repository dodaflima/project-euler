#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The sum of the squares of the first ten natural numbers is,
1² + 2² + ... + 10² = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)² = 55² = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

A soma do quadrado dos primeiros 10 números naturais é
1² + 2² + ... + 10² = 385
O quadrado da soma dos primeiros 10 números naturais é
(1 + 2 + ... + 10)² = 55² = 3025
A diferença entre o quadrado da soma e a soma dos quadrados é
3025 - 385 = 2640

Encontre a diferença entre a soma dos quadrados e o quadrado da soma dos primeiros cem números naturais
"""

number_list = list(x+1 for x in range(100))
sum_square = sum(x**2 for x in number_list)
square_sum = (sum(number_list))**2

result = square_sum - sum_square

# Answer
print(result)
