# 참고: https://docs.python.org/ko/3/library/json.html
import json
# import pickle

print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))
json.dumps("{'name':'kim', 'age': 22}") # 파일에 저장