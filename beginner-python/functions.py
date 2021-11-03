name = 'abc'
def test():
    print(f'My name is {name}')

def sq(w,h):
    v = w*h
    return v

test()
val = sq(2,4)

print(f'The sq. is {val}')

#functions and scope

x =50
def num():
    x = 10
    print(f'Value in a func{x}')

print(f'Value outside func{x}')

#global -> function -> statement scope

#Internal funcs
def counter():
    def display(count=0):
        print(f'count {count}')
    for x in range(5): display(x)

print('Internal funcs')
counter()

# *args - positional variable length anrguments
def multiply(*args):
    z = 1
    for num in args:
        print(f'num {num}')
        z *= num
    print(f'z {z}')
print('args')
multiply(1,2,3,4)

# **kargs is used to pass a keyworded, variable length arguments
def profile(**person):
    print(person)
    def display(k):
        if k in person.keys(): print(f'{k} = {person[k]}')
    display('name')
    display('age')


print('**kargs')
profile(name='salman', age=23)

# lambda funcs
# normal

def makesq(h=0,w=0):
    return w*h
print(makesq(3,2))

# lambda func
sqft = lambda h=0,w=0: w * h
print('sqft',sqft(2,2))