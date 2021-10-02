# for loop on lists, tuples, sets

l= [1,2,3,4] #list
t= (1,2,3,4) #tuple
s= {1,2,3,4} #set

for i in s:
    print(f'i={i}')

# loop on dictionary
x = dict(salman=23, ubaid=22)
print(x)

for k in x.keys():
    print(f'keys: {k} = {x[k]}')

for key,value in x.items():
    print(f'keys: {key} = {value }')

# range
x = range(5)
print(x)
for i in x:
    print(f'range: {i}')

# range, start,stop,step
x=range(5,20,3)
print(x)
for i in x:
    print(f'stepped: {i}')