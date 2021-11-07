# navigate folders

import os
d = os.getcwd()
print(f'currently in {d}')

# change folders
c=os.chdir('..')
print(f'going back" {os.getcwd()}')

# list dir
for f in os.listdir():
    print(f)
    print(f'Path: {os.path.abspath(f)}')
    if os.path.isdir(f): print(f'Dir: {f}')
    if os.path.islink(f): print(f'Link: {f}')
    if os.path.isfile(f): print(f'File: {f}')

# scan dir
print('Scan Dir------')
for e in os.scandir():
    print(e)
    print(f'Name {e.name}')
    print(f'Path {e.path}')
    if e.is_dir(): print('Dir: ', {e.name})
    if e.is_file(): print('file: ', {e.name})
    if e.is_symlink(): print('Link: ', {e.name})

# Glob
import glob
os.chdir('..')
dir = os.getcwd()

for filename in glob.glob(pathname=dir + '**/**', recursive=True):
    print(f'glob: {filename}')

print('Walk--------')
for currentpath, folders,files in os.walk('.'):
    for file in files:
        print(f'walk: {os.path.join(currentpath, file)}')