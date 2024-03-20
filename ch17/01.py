# pip install requests 
from matplotlib import pyplot as plt
import requests
import json

# api호출로 데이터 요청하기
# u = 'https://api.github.com/search/repositories?q=language:python+sort:stars' 
# res = requests.get(u)

# 안되면 python -u "C:\k6_programming\python_work\ch17\01.py" 로 실행해보기?
# print(type(res.json()))

name = []
starCnt = []

with open('./data/github_api_star.json', 'r', encoding='UTF8') as f:
    data = json.load(f)
    # print(len(data['items'])) # 30개
    for item in data['items']:
        name.append(item['name'])
        starCnt.append(item['stargazers_count'])

plt.bar(name, starCnt)
plt.xticks(rotation=-45)
plt.show()

