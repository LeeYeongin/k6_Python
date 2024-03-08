# with open('./ch10/name.txt', encoding='utf-8') as file:
#     for line in file:   
#         print(line, end='')
        # print(line.rstrip()) # (오른쪽)공백제거
    # print(file.readlines) # 파일 한번에 다 읽기

import csv

with open('./ch10/grade.csv') as file:
    reader = csv.reader(file)
    header = next(reader)
    for line in reader:
        print(line)
    print(header)