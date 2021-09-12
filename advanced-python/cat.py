class Cat:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'Constructor for {self.name} and age {self.age}')