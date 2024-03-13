import matplotlib.pyplot as plt

x  = list(range(1, 101))
square = [i**2 for i in x]
# print(x, square)

fig, ax = plt.subplots()
# ax.plot(x, square, color='red')
ax.scatter(x, square, c=square, cmap = plt.cm.Blues) # y값이 낮으면 연한 파란색, 높으면 진한 파란색
# ax.scatter(x, square)
ax.set_title('Square')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# ax.tick_params(labelsize=30)  # 틱 이름표 크기 지정
# plt.style.use('seaborn-v0_8-pastel') # 스타일 적용
# ax.ticklabel_format(style='plain') # 눈금 이름표의 기본 스타일을 덮어쓰기

# 가능한 style확인
# for s in plt.style.available:
#     print(s)

# ax.set_xlim(0, 20)
# ax.set_ylim(0, 20)
# plt.scatter(x, square, c=square, cmap = plt.cm.Blues)
# plt.colorbar()
plt.show()