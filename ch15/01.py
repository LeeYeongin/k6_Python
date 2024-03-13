import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # Create a figure containing a single axes.

def plot(x,y,label):
    ax.plot(x,y,label=label) # 선 그래프

x = [1, 2, 3, 4]
y = [2, 3, 4, 6]
plot(x,y,'blue')
# ax.scatter(x, y, label='blue')

x2 = [1, 2, 3, 4]
y2 = [1, 2, 3, 4]
# plot(x2,y2,'red')
ax.scatter(x2, y2, label='yellow') # 점 그래프

ax.set_title('Plot A and B')
ax.set_aspect('equal') # 실제비율 반영
# x,y 라벨 이름 설정
ax.set_xlabel('Age')
ax.set_ylabel('BMI')

# x,y 한계지정
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ax.legend()
plt.savefig('./ch15/plot.png')
plt.show()