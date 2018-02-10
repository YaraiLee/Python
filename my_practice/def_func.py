def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

num = my_abs(-10)
print(num)

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

ros = move(100, 100, 60, math.pi/6)
print(ros)

#TypeError: bad operand type:
#my_abs('123')

def quadratic(a, b, c):
    dert = b ** 2 - 4 * a * c
    if dert < 0:
        return (False)
    else:
        x1 = -b + math.sqrt(dert) / (2 * a)
        x2 = -b - math.sqrt(dert) / (2 * a)
        return (x1, x2)

if quadratic(1, 4, 5):
    x1, x2 = quadratic(1, 4, 4)
    print (x1, x2)

else:
    print('无解')
