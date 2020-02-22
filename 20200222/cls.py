class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('Hello my name is {}, {}'.format(self.name, self.age))

    def old(self):
        self.age += 1
        print('나이는 : {}'.format(self.age))

A = Human('SH', 12)
A.old()
A.say()

B = Human('aa', 11)
B.old()
B.say()