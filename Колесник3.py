# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:18:24 2020

@author: Batya
"""

print("Для виходу з программи(циклу) введіть 'exit'")
while True:
    s = input("Виберіть операцію (+,-,*,/,**): ")
    if s == 'exit': break
    if s in ('+','-','*','/','**'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("Результат:",x+y)
        elif s == '-':
            print("Результат:",x-y)
        elif s == '*':
            print("Результат:",x*y)
        elif s == '/':
            print("Результат:",x/y)
        elif s== "**":
            print("Результат:",x**y)
    else:
        print("Виберіть правильну операцію")