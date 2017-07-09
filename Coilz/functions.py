from Complex import Complex
import fibo


class MyMath:
    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def message(self):
        print("This is a message inside the class.")


myMath = MyMath()

a = myMath.add(3, 4)
print(a)

b = myMath.multiply(3, 4)
print(b)

b = myMath.message()


class Person:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


person = Person('coilz')
print("Person with name: " + person.name)


x = Complex(3.0, -4.5)
print (x.r, x.i)

fibo.fib(1000)
