from matplotlib import pyplot as plt
from random import randint

# 01
# x = [1,2,3,4]
# y = [i**2 for i in x]
# print(x,y)
# plt.plot(x,y)

# 02
# x = [randint(0, 9) for _ in range(1000)]
# plt.hist(x)

# 03
# x1 = list(range(1,5))
# y1 = [i**2 for i in x1]
# x2 = list(range(1,5))
# y2 = [i**3 for i in x1]


# plt.title('X Square')
# plt.xlabel('X')
# plt.ylabel('X Square')
# plt.legend()
# plt.show()

# 04
# fig, ax = plt.subplots(1,2)
# ax[0].plot(x1,y1,label='A',color='green')
# ax[0].plot(x2,y2,label='B', color='orange')
# ax[0].legend()

# ax[1].scatter(x1,y1,label='A',color='green')
# ax[1].scatter(x2,y2,label='B', color='orange')
# ax[1].legend()

# plt.show()

# 05
import csv
import datetime as dt # 모듈
from datetime import datetime # 클래스

x1, y1 = [], []
x2, y2 = [], []

with open('./ch16/weather_data/a.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)

    for row in reader:
        x1.append(datetime.strptime(row[2], '%Y-%m-%d'))
        y1.append(int(row[4]))
        y2.append(int(row[5]))
        # print(row[5])

plt.plot(x1, y1, label='TMAX', color='green')
plt.plot(x1, y2, label='TMIN', color='orange')
plt.xticks(x1, rotation='vertical')
plt.xlabel('Date')
plt.fill_between(x1, y1, y2)
plt.legend()
plt.show()
