#taking input from the user

# def calProd(a,b):
#     return a * b

# number=int(input("enter a number: "))
# for i in range(1,11):
#     print(f"{number} x {i} = {number * i}")

class Person:
    name = "Dheeraj"
    def __init__(self):
        print("init called!")

s = Person()   
print(s.name)     