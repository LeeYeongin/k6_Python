from pathlib import Path 

path = Path('./ch10/aaa/aaa.txt')
# if  path.exists(): # 방어코드
try:
    with open(path) as file: # FileNotFoundError 발생
        for line in file:
            print(line)
except Exception as e:
    pass # 에러 발생시 오류 출력하지 않고 그냥 통과