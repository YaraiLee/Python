#!/usr/bin/python
#-*-coding:UTF-8-*-

#쳲���������
#쳲��������У�Fibonacci sequence�����ֳƻƽ�ָ����У�ָ��������һ�����У�0��1��1��2��3��5��8��13��21��34��������

def fib(n):
	if 1 == n:
		return [1]
	elif 2 == n:
		return [1,1]
	fibs = [1,1]
	for i in range(2, n):
		fibs.append(fibs[-1]+fibs[-2])
	return fibs
print (fib(10))