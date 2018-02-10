import functools
#case 1
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args, **kw)
    return wrapper
#decorator
@log
def now():
    print('2017-01-18')

now()
print(now.__name__)

#case 2
# with params
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s %s():" % (text, func.__name__))
            return  func(*args, **kwargs)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2017-01-18')

now()
print(now.__name__)

#case 3
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin %s():' %func.__name__)
        x = func(*args, **kw)
        print('end %s():' %func.__name__)
        return x
    return wrapper
@log
def now():
    print('2017-01-18')
now()

#case 4

def log(set_in=None):

# 装饰器参数为：可选
# 默认结构为：  带输出信息的三层装饰器结构
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if callable(set_in):
                print('call: %s' % func.__name__)
            else:
                print('call(\'%s\'): %s' % (set_in, func.__name__))
            return func(*args, **kw)

        return wrapper


    if callable(set_in):  # 如果传入的set_in是函数
        return decorator(set_in)  # 把函数作为参数传给decorator，逻辑上减少一层级
    else:
        return decorator  # 如果传入的set_in非函数，decorator默认参数会自动获得函数


@log
def test1():
    print('func 1 inside')


@log('another test:')
def test2():
    print('func 2 inside')

test1()
test2()