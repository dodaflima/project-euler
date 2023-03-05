#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

A sequência de Fibonacci é definida pela relação de recorrência:
Fn = Fn-1 + Fn-2, onde F1 = 1 e F2 = 1.
Assim os primeiros 12 termos serão:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
O 12° termo, F12, é o primeiro termo a conter 3 digitos.
Qual é o index do primeiro termo na sequência de Fibonacci a conter 1000 digitos?
'''

one_thousand_digits = lambda x: len(str(x)) == 1000

def answer():
    fib_list = [1, 1]
    while not one_thousand_digits(fib_list[-1]):
        fib_list.append(sum([fib_list[-1], fib_list[-2]]))
    
    return fib_list.index(fib_list[-1]) + 1

# Answer
print(answer())
        