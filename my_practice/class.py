#!/usr/bin/python3

class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'

x = MyClass()

print("MyClass 类的属性i为: ", x.i)
print("MyClass 类的方法f输出为: ", x.f())

class Complex:
    """带参数构造函数"""
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)

print(x.i, x.r)

"""类的方法"""
class people:
    """类的基本属性"""
    name = ''
    age = 0
    """类的私有属性，私有属性在类的外部无法直接访问"""
    __weight = 0
    #定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说:我 %d 岁。" %(self.name, self.age))
#单继承示例
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        #调用父类的构造函数
        people.__init__(self, n, a, w)
        self.grade = g
    #复写父类的方法
    def speak(self):
        print("%s 说:我%d岁了， 我在读%d年级"%(self.name, self.age, self.grade))

#另一个类，多继承之前的准备
class speaker():
    topic = ''
    name  = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫%s,我是一个演说家，我演讲的主题是%s" %(self.name, self.topic))

#实例化类
p = people('W3cchool', 10, 30)
p.speak()

s = student('ken', 10, 60, 3)
s.speak()

#多重继承
class sample(speaker, student):
    a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

test = sample("Tim", 25, 80, 4, "python")
test.speak()#方法同名，默认调用括号中排前的父类方法

#方法重写
class Parent:
    def myMethod(self):
        print("调用父类方法")

class Child(Parent):
    def myMethod(self):
        print("调用子类方法")


c = Child()
c.myMethod()

#类的私有变量
class JustCounter:
    __secretCount = 0 #私有变量
    publicCount = 0   #共有变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
#print(counter.__secretCount)#报错，实例不能访问私有变量

##运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a+other.a, self.b+other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1+v2)