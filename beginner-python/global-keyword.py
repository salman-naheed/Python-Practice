# global
x = 1
def test():
    x = 6
    print(f'in func:{x}')

test()
print(x)

# global var
counter = 0

def count(max):
