def lazy_sum(args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum
L = [1,3,5,7]
f1 = lazy_sum(L)
f2 = lazy_sum(L)
print(f1 == f2)
print(f1())
print(f2())

def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1(), f2(), f3())


def count():
    fs = []
    for i in range(1, 4):
        def f(n=i):
            return n * n
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())

