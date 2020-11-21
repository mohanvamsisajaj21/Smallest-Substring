# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 19:54:54 2020

@author: mohan
"""

def max_distinct(s, n): #Finding the number of distinct characters in a string
    arr = [] #An Array which contains all the unique elements of the given string
    for i in s:
        if(i not in arr):
            arr.append(i)
    return len(arr)

def smallest_sub(s): #Finding length of smallest substring with distinct characters
	n = len(s)
	md = max_distinct(s, n) 
	min = n
	for i in range(n): 
		for j in range(i, n): #Checking all the substrings of the string
			x = s[i:j] 
			l = len(x) 
			sub_dis = max_distinct(x, l)
			if(l<min and md==sub_dis): #Checking if the given substring satisfies our conditions
				min = l 
	return min
 
s = str(input())
n = smallest_sub(s); 
print(n) 
