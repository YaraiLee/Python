#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
"""
print ("hello, python!")

if True:
	print ("True")
else:
	print ("False")
"""
###List
"""
list=['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print (list)
print (list[0])	
print (list[1:3])
print (list[:3])
print (list[3:])
print (list[-3:-1])
print (tinylist*2)
print (list+tinylist)
"""
##tuple
"""
tuple = ('runoob', 786, 2.23, 'john', 70.2);
tinytuple = (123, 'hohn')

print (tuple)
print (tuple[0])
print (tuple[1:3])
print (tinytuple * 2)
print (tuple+tinytuple)
"""

##dict
"""
dict = {}
dict['one'] = "There is one"
dict[2] = 'This is two'

tinydict={'name':'john', 'code':6734, 'dept':'sales'}

print (dict['one'])
print (dict[2])
print (tinydict)
print (tinydict.keys())
print (tinydict.values())
"""
##while-loop
"""
var = 1
while var == 1:
	num = input("Enter a number :")
	print ("You entered:", num)
	
print ("Good bye!")
"""
##for-loop
"""
for num in range(10, 20):
	for i in range(2, num):
		if num % i == 0:
			j = num/i
			print ('%d 等于 %d * %d' %(num, i, j))
			break
	else:
		print (num, '是一个质数')
"""
##break
var = 10
while var > 0:
	print ('当前变量值:', var)
	var -= 1
	if var == 5:
		break
		
print ("Good bye!")
os.system("pause")