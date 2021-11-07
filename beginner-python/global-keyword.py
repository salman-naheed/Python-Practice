# global
x = 1
def test():
    x = 6
    print(f'in func:{x}')

test()
# print(x)

# global var
counter = 0

# scope issues
def count(max):
    global counter
    counter += 1
    if counter >= max: return False
    return True

limit = 5
for x in range(limit):
    b = count(limit)
    print(counter)

print('Done')

