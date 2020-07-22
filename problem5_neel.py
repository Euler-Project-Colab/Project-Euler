#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:26:50 2020

@author: neel
"""
"""
Program
"""
import math
import numpy as np
from sympy import sieve
import time




#Elegant and Fast method using GCD between current answer
t=time.time()

ans = 1
for i in range(1, 21):  
    ans = int((ans * i)/math.gcd(ans, i)) 
print(ans)
print("time = ",time.time()-t)  



#Complex Method
t=time.time()
primes = list(sieve.primerange(1, 20))
length=len(primes)
frequency_array=np.zeros(length,dtype=int)
array = np.arange(2,21)
i=0
j=0
for x in range(2,21,1):
    for y in primes:
        while x%y==0:
            i=i+1
            x=x/y
        if (frequency_array[j]<i):
            frequency_array[j]=i
        j=j+1
        i=0
    j=0
answer=1
for x in frequency_array:
    answer=answer*(primes[j]**x)
    j=j+1
print(answer)
print("time = ",time.time()-t)  

