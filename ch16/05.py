import json
import plotly.express as px #  pip install plotly-express 사용을 위해 설치

# json load  - file
# json loads - str -> dict, dict -> str

# 160개
mag = [] # 지진 규모
lat = [] # 위도
lon = [] # 경도

with open('./data/b.geojson', 'r', encoding='UTF8') as f:
    data = json.load(f)
    for feature in data['features']:
        # print(feature['geometry']['coordinates'])
        mag.append(feature['properties']['mag'])
        lon.append(feature['geometry']['coordinates'][0])
        lat.append(feature['geometry']['coordinates'][1])

fig = px.scatter_geo(lat=lat, lon=lon, size=mag)
fig.show()    
    
    # 데이터 형식을 확인하기 위한 출력 ↓
    # print(type(data))
    # print(data['type'])
    # print(type(data['metadata']), data['metadata'])
    # print(type(data['metadata']['count']), data['metadata']['count']) # 숫자는 알아서 int 타입으로 인식
    # print(type(data['features']), data['features'][0])
    # # 필요한 정보: feature > geometry > coordinates 
    # print(data['features'][0]['geometry']['coordinates'])

