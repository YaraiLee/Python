#!/usr/bin/python
#-*- coding: UTF-8 -*-
#��Ŀ����ӡ�����е�"ˮ�ɻ���"����ν"ˮ�ɻ���"��ָһ����λ�������λ���������͵��ڸ������������磺153��һ��"ˮ�ɻ���"����Ϊ153=1�����η���5�����η���3�����η���

for n in range(100, 1000):
	i = n // 100
	j = n // 10 % 10
	k = n % 10

	if n == (i ** 3 + j ** 3 + k ** 3):
		print (n)