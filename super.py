class A:
    class_var1 = 'class A'
    def __init__(self):
        self.var1 = 'var1'
        self.class_var1 = 'self class var1'
        self.special = 'special'

class B(A):
    # class_var1 = 'class B'

    def __init__(self):
        self.var1 = 'var2'
        self.class_var1 = 'self class var2'
        super().__init__()
        print(super().class_var1)

a =B()
