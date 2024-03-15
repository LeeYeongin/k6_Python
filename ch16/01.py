# import pandas as pd
# pd.read_csv('./ch16/weather_data/a.csv')

# with open('./ch16/weather_data/a.csv') as f:
#     for line in f:
#         print(line.rstrip().split(sep=','))

from datetime import datetime
from pathlib import Path
import csv
from matplotlib import pyplot as plt

COL_DATE = 2
COL_TMAX = 4 # full: 7?
COL_TMIN = 5 # full: 8?
x1, y1 = [], []
x2, y2 = [], []

with open(Path('ch16/weather_data/', 'a.csv')) as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        # print(line, type(line))
        x1.append(datetime.strptime(line[COL_DATE], '%Y-%m-%d'))
        y1.append(int(line[COL_TMAX]))
        x2.append(datetime.strptime(line[COL_DATE], '%Y-%m-%d'))
        y2.append(int(line[COL_TMIN]))

# for idx, h in enumerate(header):
#     print(idx, h)

# print(f'x: {x1}')
# print(f'y: {y1}')

plt.plot(x1,y1,label='TMAX')
plt.plot(x2,y2,label='TMIN')
plt.fill_between(x1, y1, y2, alpha=0.1)
plt.legend()
plt.show()