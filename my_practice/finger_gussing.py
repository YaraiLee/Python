﻿#-*-coding:UTF-8-*-
import random
while 1:
	s = int(random.randint(1, 3))
	if 1 == s:
		ind = "石头"
	elif 2 == s:
		ind = "剪子"
	elif 3 == s:
		ind = "布"
	m = input("输入 石头、剪子、布，输入'end'结束游戏:")
	blist = ['石头','剪子','布']
	if (m not in blist) and (m != 'end'):
		print ('输入错误，请重新输入!')
	elif (m not in blist) and (m == 'end'):
		print ('\n游戏退出中...')
		break
	elif (m == ind):
		print ("电脑出了:" + ind + ", 平局！")
	elif (m == '石头' and ind == '剪子') or (m == '剪子' and ind == '布') or (m == '布' and ind == '石头'):
		print ("电脑出了:" + ind + ", 你赢了！")
	elif (m == '石头' and ind == '布') or (m == '剪子' and ind == '石头') or (m == '布' and ind == '剪子'):
		print ("电脑出了：" + ind + "，你输了！")