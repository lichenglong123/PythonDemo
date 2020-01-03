class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print("我饿了")
            self.hungry=False
        else:
            print("我吃饱了，哈哈哈")





class Songbird(Bird):
    def __init__(self):
        super().__init__()
        self.sound="好日子"
    def sing(self):
        print(self.sound)



s=Songbird()
s.sing()
s.eat()





