def funcargs(normal,*agrs,**kwargs):
    print(normal)

    for i in agrs:
        print(i)

    for key,value in kwargs.items():
        print(f"This is {key} and he work at {value}")


har = ['salman', 'ubaid', 'hammad']
normal = "Hi Call me salman."
kargs = {"Salman": "Meisasoft", "Ubaid": "Meisasoft", "Hammad": "Mern Stack"}
funcargs(normal,*har,**kargs)
