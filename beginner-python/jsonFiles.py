import json
fileName = 'json.txt'

# to string
outD = dict(name='salm', age=23)
s = json.dumps(outD)
print(f'string= {s}')

# to file
with open(fileName, 'w') as f:
    json.dump(outD,f)

inD = json.loads(s)
print(f'load :{inD}')

# load from file
with open(fileName, 'r') as f:
    FD = json.load(f)
print(f'Type: {type(FD)}')