# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 17:40:21 2020

@author: Batya
"""
from random import randint
 
tmp = []
while len(tmp) < 3:
    x = randint(1, 101)
    if x not in tmp:
        tmp.append(x)
 
print(*tmp)