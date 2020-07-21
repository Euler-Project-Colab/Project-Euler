#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:17:09 2020

@author: neel
"""
"""
Program to print out sum of all even numbers in Fibonacci seq<4000000
"""
#initialize starting terms
a=1
b=2
c=0
list=[1,2]
even_list=[2]
while((a+b)<4000000):
    c=a+b
#update terms
    a=b
    b=c
#add element to list
    if(c%2==0):
        even_list.append(c)

#sum function on list
sum_even=sum(even_list)
print(sum_even)
#Answer=4613732