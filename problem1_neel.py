#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:58:24 2020

@author: neel
"""
"""
Program to print out sum of all multiples of three or five below 1000
"""
sum=0
for i in range(0,1000,3):
#Add numbers divisible by 3
    sum=sum+i;
for i in range(0,1000,5):
#Add numbers divisible by 5
    sum=sum+i;
for i in range(0,1000,15):
#Subtract numbers divisible by 15
    sum=sum-i;
print(sum)
#Answer=233168
#Using Arithmetic Progression would be a more viable way 
