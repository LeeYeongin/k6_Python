from pathlib import Path

path = Path('ch10','aaa','aa.txt')

with open(path, 'w') as file: # 기존에 파일이 있다면 덮어쓰기됨
    file.write('b\n')
    file.write('bb\n')
    file.write('bbb\n')

# with open(path, 'a') as file: # 이어서 작성
#     file.write('aaa\n')
#     file.write('aa\n')
#     file.write('a\n')