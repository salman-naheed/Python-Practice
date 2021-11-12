# write a text file
import os
# simply mode usage

def toFile(fileName, mode, data):
    f = open(fileName,mode)
    for i in range(5):
        f.write(str(i) + ':' + data + '\r\n')
    f.close()

# write will overwrite file
def wrtieFile(fileName):
    toFile(fileName, 'w', 'Hello its me')

def appendFile(fileName):
    toFile(fileName,'a', 'hello again')

def readFile(fileName):
    if not os.path.exists(fileName):
        print('File not found')
        return
    f = open(fileName, 'r')
    print(f.read())
    f.close()

myfile = 'hi.txt'
wrtieFile(myfile)
appendFile(myfile)
readFile(myfile)