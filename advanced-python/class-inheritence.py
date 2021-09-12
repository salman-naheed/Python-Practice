class Feline:
    def __init__(self, name):
        self.name = name
        print('Feline')

    def meow(self):
        print(f'{self.name} meow')

    def setName(self,name):
        print(f'{self} setting name: {name}')
        self.name = name

class Lion(Feline):
    def roar(self):
        print(f'{self.name} roar')

class Tiger(Feline):
    def __init__(self):
        print('Tiger')

    def stalk(self):
        print(f'{self.name} stalking')

    def rename(self,name):
        super().setName(name)

c = Feline('kitty')
print(c)
c.meow()

l=Lion('Leo')
l.meow()

t = Tiger()
print(t)