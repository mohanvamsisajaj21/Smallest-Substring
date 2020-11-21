# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 19:54:54 2020

@author: mohan
"""

def max_distinct(s, n): 
	arr = [0]*256
	for i in range(n): 
		arr[ord(s[i])]+=1
	md = 0
	for i in range(256): 
		if(arr[i]>0): 
			md+=1	
	return md

def smallest_sub(s): 
	n = len(s)
	md = max_distinct(s, n) 
	min = n
	for i in range(n): 
		for j in range(i, n): 
			x = s[i:j] 
			l = len(x) 
			sub_dis = max_distinct(x, l)
			if(l<min and md==sub_dis): 
				min = l 

	return min
 
s = str(input())
n = smallest_sub(s); 
print(n) 
