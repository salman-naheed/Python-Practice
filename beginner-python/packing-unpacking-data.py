# packing data
# problem with args and kwargs is we can not use lists and dicts
def pack(*num):
    print(f'Packed: {num}')
    for x in num:
        print(f'Packed: {x}')

pack(1,2,3)

# unpacking
def unpack(a,b,c):
    print(f'unpacked: {a, b , c}')

list = [1,2,3]
unpack(*list)

# dictionary issue
d = dict(name='sal', age=12)

# packing dictionary
pack(*d)
# unpacking dictionary
# unpack(*d)

# packing a dict
def packDict(**nums):
    print(f'packing Dict: {nums}')
    for k in nums:
        print(f'packed: {k} = {nums[k]}')
packDict(name='salman', age=23)

# unpacking a dict
def unpackDict(name,age):
    print(f'unpacking dict: {name, age}')

d = dict(name='salm', age=10)
unpackDict(**d)