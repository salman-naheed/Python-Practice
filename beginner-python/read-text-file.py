# reading a text file CMS

# get a filename
import os, sys

print(f'File: {__file__}') #built in file name
print(f'args: {sys.argv}')
sfile = os.path.abspath(sys.argv[0])
print(f'Read file: {sfile}')

# exists
if not os.path.exists(sfile):
    print('File not found!')
    exit(1)

# open a file
f = open(sfile,'r')
# read a line
line = f.readline()
print(f'line', line)

# read number of letters
chars = f.read(10)
print(f'chars: {chars}')

# position
print(f'position: {f.tell()} of {os.stat(sfile).st_size}')

# seek
f.seek(0)

# read all lines
for l in f.readlines():
    print(l.strip())

# close the file
f.close()