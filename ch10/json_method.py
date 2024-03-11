# 참고: https://docs.python.org/ko/3/library/json.html
import json

print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))
json.dumps("{'name':'kim', 'age': 22}") # 파일에 저장

# 메모리(서버) -> dump -> file(사용자 컴퓨터)
# file(사용자 컴퓨터) -> load -> 메모리(서버)
data = '{"name": "kim", "age": 23}'
data2 = {"name": "kim", "age": 23} # dict 형태

# 파일 작성
with open('./ch10/member.json','w') as file:
    json.dump(data, file)

with open('./ch10/member2.json','w') as file:
    json.dump(data2, file)

# 파일 읽기
with open('./ch10/member2.json', 'r') as file:
    d = json.load(file)
    print(d)

d2 = json.dumps(data2)
print(d2, type(d2)) # type = str

d3 = json.loads(d2) # loads는 string or buffer 사용가능
print(d3, type(d3), d3["name"]) # type = dict, key값으로  value 접근 가능

import pickle

d = [1,2,3,4,5]
with open('./ch10/dump_member.pk','w') as file:
    json.dump(d, file)

with open('./ch10/dump_member.pk','r') as file:
    data3 = json.load(file)
    print(data3)