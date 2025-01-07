class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def show_details(self):
        print("Role =",self.role)
        print("Dept =",self.dept)
        print("Salary =",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","60,000")


eng1=Engineer("Narendra",24)
eng1.show_details()
eng2=Engineer("Vidit",25)
eng2.show_details()