# Simple app - paint calculator

print('Enter a wall size as width,height in feet or press enter to stop')
print('Example:12,8')

#variables

walls= []
gallons = 1/350 #one gallons covers 350sqft
total = 0

while True:
    s = input('Enter wall size: ')
    if len(s)==0: break

    sqft = s.split(',')
    if len(sqft) < 2:
        print('invalid format')
        break
    w = int(sqft[0])
    h = int(sqft[1])
    item = [w,h]
    walls.append(item)
    print(f'adding wall: {item}')

#calculation
print(f'you entered {walls}')
for m in walls:
    w=m[0]
    h= m[1]
    s= w*h
    v= s*gallons
    total += v

print(f'buy {round(total,2)} gallons of paint')