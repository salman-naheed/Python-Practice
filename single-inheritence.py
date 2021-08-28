class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def changeLeaves(cls, newLeave):
        cls.no_of_leaves = newLeave

    @classmethod
    def newMethod(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])

    @staticmethod
    def printgoods(string):
        print("Hey" + string)

class Programmer(Employee):
    def progDetails(self):
        return f"hey ${self.name}"

harry = Employee('salman', 123, 'admin')
salman = Employee('har', 344, 'stu')

# newPass = Employee.newMethod("salman-786-admin")
# salman.changeLeaves(34)
callme = Programmer('sal')
print("prog", callme.progDetails())