#!/usr/bin/python3
# -*- coding: utf8 -*-

#操作系统接口
import os
print(os.getcwd())
#os.system('mkdir test')
#os.chdir('F:\liyalei')
#print(os.getcwd())

print(dir(os))
#print(help(os))


#import shutil
#shutil.copyfile('data.db', 'archive.db')
#shutil.move('/build/executables', 'installdir')

#文件通配符
import glob
print(glob.glob('*.py'))

#命令行参数
import sys
print(sys.argv)

#错误输出重定向和程序终止
sys.stderr.write('error!\n')
sys.exit()