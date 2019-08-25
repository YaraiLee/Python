from functools import reduce


# example list
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 9]))


# example string
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(fn, map(char2num, '1230')))


# work 1
def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# work 2
def fn(x, y):
    return x * y


def prod(L):
    return reduce(fn, L)


print('3*5*7*9 = ', prod([3, 5, 7, 9]))


# work 3
def char2int(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def fn(x, y):
    return x * 10 + y


def str2float(str):
    index = str.index('.')
    str_1 = str[:index]
    str_2 = str[index + 1:]
    n = len(str_2)

    return reduce(fn, map(char2int, str_1)) + reduce(fn, map(char2int, str_2)) * (0.1 ** n)


print(str2float('12034.5607'))
