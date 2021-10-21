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

#args
def multiply(*args):
    z = 1
    for num in args:
        print(f'num {num}')
        z *= num
    print(f'z {z}')
print('args')
multiply(1,2,3,4)