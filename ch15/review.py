from matplotlib import pyplot as plt
import random

from matplotlib.ticker import MultipleLocator

# x = [random.randint(0, 9) for _ in range(10000)]
# y = [i**2 for i in x]

# plt.plot(x,y)
# plt.scatter(x,y)
# plt.hist(x)
# plt.show()
# ----------------------------------------------------#

x1 = list(range(5))
y1 = [i**2 for i in x1]

x2 = list(range(5))
y2 = [i**3 for i in x2]

fig, ax = plt.subplots()
ax.plot(x1, y1, label="AAA", color="red", linewidth=3)
ax.plot(x2, y2, label="BBB", color="green")
ax.scatter(x1, y1, color="red")
ax.scatter(x2, y2, color="green")

ax.set_title('AAA vs BBB')
ax.set_xlabel('x')
ax.set_ylabel('y')

# x축 눈금 바꾸기
ax.set_xticks([0,1,2,3,4]) 
# ax.xaxis.set_major_locator(MultipleLocator(1)) # 위와 동일한 결과

plt.legend()
plt.show()