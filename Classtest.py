# coding=utf-8

def start(obj):
    obj.speak()

class Animal:
    def speak(self):
        print("动物会说话~")


class Dog(Animal):
    def speak(self):
        print("小狗说话汪汪汪~")


class Cat(Animal):
    def speak(self):
        print("小猫说话喵喵喵~")

class Car:
    def speak(self):
        print("小汽车说话嘀嘀嘀~")


start(Dog())
start(Cat())
start(Car())