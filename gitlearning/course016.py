# 面向对象编程

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print(f'{self.name}正在学习{course_name}')

    def play(self):
        print(f'{self.name}正在玩耍')


s1 = Student('xiaoxiao',20)
s1.study('语文')