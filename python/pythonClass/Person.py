from abc import ABC,abstractmethod

class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def _Person__greet(self):
        print("Hello word I'm{}.".format(self.name))


class Caculate:
    def getValue(self):
        print("1000")

    def sayHello(self):
        print(" Caculate hello word")


class Say:
    def sayHello(self):
        print(" Say hello word")

    def getValue(self):
        print("20000")


class All(Say, Caculate):
    pass

print("===============")

class Talk(ABC):
    @abstractmethod
    def say(self):
        pass






print(type(str))




