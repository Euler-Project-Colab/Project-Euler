#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 23:21:04 2020

@author: neel
"""
"""
Program to print largest palindrome found by multiplying two 3 digit numbers
"""

# import time
#funtion to check if a number is palindrome
def chk_palindrome(num):

    temp = num[:]

    temp.reverse()
    if temp == num:
        return True

    return False

# t = time.time()

max_palindrome = 0
#slightly slower, more readable method
# for i in range(999, 316, -1):

#     for j in range(i, 316, -1):

#         if i*j < max_palindrome:
#             break

#         if((i*j)%11==0 and chk_palindrome(list(str(i*j)))):
#             max_palindrome = i*j

#check in appropriate ranges
for i in range(990, 316, -11):
    
    for j in range(999, 316, -1):
        if i*j < max_palindrome:
            break

        if(chk_palindrome(list(str(i*j)))):
            max_palindrome = i*j
print (max_palindrome)
# print (time.time() - t)
#answer= 906609