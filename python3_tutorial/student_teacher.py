#!/usr/bin/env python3
from collections import Counter
import sys

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self):
        return self.name               


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        c = Counter(sys.argv[2])
        return "Pass: {}, Fail: {}".format(sum(c.values())-c['D'], c['D'])     

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        c = Counter(sys.argv[2])
        c = c.most_common()
        str1 = ''
        for i in range(3):
            str1 += str(c[i][0]) + ': ' + str(c[i][1]) + ', '
        str1 += str(c[3][0]) + ': ' + str(c[3][1])
        return str1

person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

if sys.argv[1] == 'student':
    print(student1.get_grade())
else:
    print(teacher1.get_grade())
