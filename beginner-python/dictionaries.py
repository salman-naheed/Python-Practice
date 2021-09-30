#Dictionaries {k:v,k:v}
#index by keys, any immutable type

d = {'key': 'dog', 'age': 6,'name':'spot'}
print(d)

d = dict(key='dog', age=5, name='spot')
print(d)

#get keys and values
print(f'items: {d.items()}')
print(f'keys: {d.keys()}')
print(f'val: {d.values()}')

#get value from key
print(f'age: {d["age"]}')

#add item
d['trick'] = 'sit'
print(d)
d['trick'] = 'hi'
print(d)

#remove
del d['trick']
print(d)

if 'name' in d:
    print('its in')

for key in d.keys():
    print(f'{key} = {d[key]}')