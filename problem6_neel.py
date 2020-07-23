#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 18:03:32 2020

@author: neel
"""
"""
Program to calculate difference between square of first 100 numbers and sum of first 100 numbers squared
"""

import numpy as np
import time
t=time.time()
#array of first 100 integers
array=np.arange(1,101)
#solving formula
print(sum(array)**2-sum(np.square(array)))
print(time.time()-t)