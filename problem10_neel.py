#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:12:56 2020

@author: neel
"""


"""
Program to calculate sum of all Prime numbers less than 20000000
Note: Python libraries are superfast, always implement them wherever possible
"""
import sympy
import time
import numpy as np






t=time.time()
prime_list=list(sympy.primerange(1,2000000))
print (sum(prime_list))
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
t=time.time()
sum=5
for i in range(1, 2000000):
    if(chk_prime(i)):
        sum+=i
print(sum)
print(time.time()-t)








t=time.time()
sum=0
for i in range(1, 2000000):
    if(sympy.isprime(i)):
        sum+=i
print(sum)
print(time.time()-t)
