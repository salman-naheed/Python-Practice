class Employee():
    def __init__(self, aname,aroll,acity):
        self.name = aname
        self.roll = aroll
        self.city = acity

    def printDetails(self):
        return f'Name is {self.name}, Roll is {self.roll}'


call = Employee('salmmaaann',12,'ins')

print(call)
print(call.printDetails())