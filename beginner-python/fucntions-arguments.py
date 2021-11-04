# funcs and arguments

def test(name,age):
    print(f'name : {name}')
    print(f'age : {age}')

def getData():
    return dict(name='salm', age=23)

d = getData()

test(**d)

# functions as an arg
def func(data):
    d = data()
    print(f'data: {d}')

func(getData)