#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:52:01 2020

@author: neel
"""
"""
Program to print maximum prime factor of a number
"""
# import time
import math
n=600851475143
#as long as number is even
# t=time.time()
while n % 2 == 0:
    max_prime = 2
    n = n/2
#after number becomes odd, max prime is root of the number 
for i in range(3, int(math.sqrt(n)) + 1, 2):
     while n % i == 0:
         max_prime = i
         n = n / i
#prime number greator than two and odd equivalent of number less than 9
if n > 2:
    max_prime = n

print(max_prime)
# print(time.time()-t)
#answer= 6857