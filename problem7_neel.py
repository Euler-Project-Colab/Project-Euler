#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 18:22:58 2020

@author: neel
"""

"""
Program to calculate 10,001st prime number
"""
import numpy
from sympy import prime
import time
#using sympy libraries
t=time.time()
primes = prime(10001)
print(primes)
print(time.time()-t)

def chk_prime(num):
    if num == 1:
        return False
    
    i = 2
    if not((num+1)%6==0 or (num-1)%6==0):
            return False
        
    # This will loop from 2 to sqrt(x)
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

#using optimized brute-force approach
t=time.time()
chk=2
i=1
while chk<10001:
    if (chk_prime(i)):
        chk+=1
    i+=1
print(i-1)
print(time.time()-t)
#this goes on to show how fast optimized python libraries are, their use is preferred in general day projects