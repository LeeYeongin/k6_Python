import os
from pathlib import Path 

file_path = Path('./ch10/aaa/a.txt') # window/linux에서 다르게 표기되는것을 신경쓰지 않기위한 처리?
print(file_path)
dir_path = Path('./ch10/aaa')
print(dir_path)

print(os.path.isdir(dir_path))
print(os.path.isdir(file_path))

for i in os.listdir():
    print(i, os.path.isdir(i))
    if '.md' in i:
        print('found')

no_file = Path('./ch10/aaa/b.txt')
print(os.path.exists(no_file))
print(os.path.exists(file_path))

print(os.path.split(file_path))
print(Path('ch10','aaa','a.txt'))

# top = Path('.')
# print(top)