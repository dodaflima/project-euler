#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
The series, 1¹ + 2² + 3³ + ... + 10¹⁰= 10405071317.
Find the last ten digits of the series, 1¹ + 2² + 3³ + ... + 10001000.

A sequência, 1¹ + 2² + 3³ + ... + 10¹⁰ = 10405071317.
Encontre os últimos dez digitos da sequência , 1¹ + 2² + 3³ + ... + 1000¹⁰⁰⁰.
'''

answer = sum(((x+1)**(x+1)) for x in range(1000))

# Answer
print(str(answer)[:-11:-1][::-1])