class Emp():
    no_leaves = 9
    pass

print(Emp.no_leaves)
salman = Emp()

a= salman.no_leaves = 99
print(a)