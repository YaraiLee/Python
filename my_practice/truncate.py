#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("runoob.txt", "r+")
print "文件名为: ", fo.name

line = fo.readline()
print "读取第一行: %s" % (line)
	# 截断剩下的字符串
fo.truncate()
	# 尝试再次读取数据
line = fo.readline()
print "读取数据: %s" % (line)

	# 关闭文件
fo.close()
