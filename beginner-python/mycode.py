# imports
name = 'salman'

def greet():
    print(f'name: {name}')

def toFile(filename):
    global name
    with open(filename, 'w') as f:
        f.write(name)

def fromFile(filename):
    global name
    with open(filename, 'r') as f:
        name = f.read()