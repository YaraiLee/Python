#!/usr/bin/python

import time

t = (2016, 9, 13, 15, 4, 20, 2, 233, 0)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
