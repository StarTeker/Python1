# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:43:04 2020

@author: Student
"""


x1=float(input('x1='))
y1=float(input('y1='))
x2=float(input('x2='))
y2=float(input('y2='))
x3=float(input('x3='))
y3=float(input('y3='))
x4=float(input('x4='))
y4=float(input('y4='))
a=abs(((x2-x1)**2+(y2-y1)**2)**0.5)
b=abs(((x3-x2)**2+(y3-y2)**2)**0.5)
c=abs(((x4-x3)**2+(y4-y3)**2)**0.5)
d=abs(((x4-x1)**2+(y4-y1)**2)**0.5)
p=0.5*(a+b+c+d)
S= ((p-a)*(p-b)*(p-c)*(p-d))**0.5
print(round(S,3))


