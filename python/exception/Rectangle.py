class Rect:
    def __init__(self):
        self.width=0
        self.height=0

    def set_size(self,size):
        self.height,self.width=size

    def get_size(self):
        return self.width,self.height

    size=property(get_size,set_size)
    @staticmethod
    def function1():
        print("11111111111")
    @classmethod
    def function2(cls):
        print("11111111111")

r=Rect()
Rect.function1()
Rect.function2()
r.function2()
r.function1()





