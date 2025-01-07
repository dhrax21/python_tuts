class Person:
    __name="yogi"
    def __init__(self):
        print("constructor called!")

    def hello(self):
        print("Hello ",self.__name)

p1=Person()
# del(p1)
print(p1.hello())


