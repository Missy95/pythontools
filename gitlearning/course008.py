# 函数和模块
def add(a=0, b=0, c=0):
    return a + b + c

# 可变参数
def sum(*args):
    total = 0
    for x in args:
        total += x
    return total