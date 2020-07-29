#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:51:44 2020

@author: neel
"""
"""
Program to calculate special pythogorean triplet with perimeter=1000
"""
bool=False
for a in range (1,334):
    for b in range (1, 501):
        c=1000-a-b
        if(c*c==a*a+b*b):
            print(a*b*c)
            bool=True
            break
    if(bool):
        break

