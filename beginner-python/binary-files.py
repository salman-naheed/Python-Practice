# working with binary files

import random
import operator

def randomBytes(size):
    bytes = []
    for x in range(size):
        bytes.append(random.randrange(0,255))
    return bytes

def displayBytes(bytes):
    print("-"*20)
    for index,item in enumerate(bytes,start=1):
        print(f'{index}: {item} ({hex(item)})')
    print('-'*20)

b = randomBytes(20)
displayBytes(b)

# write bytes
def writeBytes(fileName,bytes):
    with open(fileName,'wb') as file:
        for b in bytes:
            file.write(b.to_bytes(1,byteorder='big'))

# read bytes
def readBytes(fileName):
    bytes=[]
    with open(fileName,'rb') as file:
        while True:
            b = file.read(1)
            if not b:
                break
            bytes.append(int.from_bytes(b,byteorder='big'))
    return bytes

outbytes = randomBytes(10)
displayBytes(outbytes)

fileName = 'hi.txt'
writeBytes(fileName, outbytes)

inbytes = readBytes(fileName)
displayBytes(inbytes)
print(f'Match: {operator.eq(outbytes, inbytes)}') 