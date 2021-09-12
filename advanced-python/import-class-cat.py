from cat import Cat

def test():
    b = Cat('first-cat', 10)
    c = Cat('second', 1)
    b.meow()

if __name__ == "__main__":
    x= Cat('test', 3)
    print(x)
    test()
