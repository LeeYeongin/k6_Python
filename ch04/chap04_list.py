# range함수
for value in range(1,5): # 1이상 5미만
    print(value)
print()

for value in range(6): # 언급하지 않으면 0부터 시작
    print(value)
print()

# python은 값에 따라 알아서 type결정
# numbers = set(range(6)) # -> {0, 1, 2, 3, 4, 5}
numbers = list(range(6)) # -> [0, 1, 2, 3, 4, 5]
print(numbers)
numbers = list(range(1, 10, 2)) # 1이상 10미만까지 2씩 건너뛰며
print(numbers)

# https://codetorial.net/tips_and_examples/list_slicing.html -> 참고 사이트
squares = [] # 대괄호이므로 list 변수
for value in range(1, 11): # :은 블록 시작을 의미
    squares.append(value**2)

print(squares)
print(value) # for문이 끝나도 값은 계속 사용 가능

# slicing 
squares = [value * 2 for value in range(1,11)]
print(squares)
print(squares[0:3]) # 0~2번째 값만 자름
print(squares[-5:-2]) # 뒤에서 5번째부터 뒤에서 2번째 앞까지
# list[start:end:step]
print(squares[::2]) # '처음'부터 끝까지 간격 2 단위로 슬라이싱
print(squares[::-2]) # '뒤'에서부터 처음부터 끝까지 간격 2 단위로 슬라이싱
print()

# 참고 사이트
# https://velog.io/@jsomedev/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8List-2%EC%B0%A8%EC%9B%90-%EB%A6%AC%EC%8A%A4%ED%8A%B8-slicing-sorting-%EA%B9%8A%EC%9D%80-%EB%B3%B5%EC%82%AC-vs-%EC%96%95%EC%9D%80-%EB%B3%B5%EC%82%AC
# 리스트의 덧셈
a = [1,2]
b = [3,4]
c = a + b
print(c)

# 리스트의 뺄셈은 없으므로 다른 방식으로 구현
a = [1,2,3,4]
b = [3,4]
c1 = [x for x in a if x not in b]
c2 = list(set(a) - set(b))
print(c1)
print(c2)
print()

a = [10, 20, 30, 40, 50]
b = a # shallow copy(실제 값이 아닌 참고하고 있는 '주소값' 복사)
c = a[:] # deep copy('실제 값'을 새로운 메모리 공간에 복사)
a[0] = 100
print(b) # a의 값만 바꿨는데 b의 값도 바뀜(shallow copy이기 때문)
print(c) # a의 값을 바꿔도 c의 값에 영향 X(deep copy이기 때문)
print()

a = [[1,2,3],[4,5,6]]
b = a[:] # shallow copy
print(b) #[[1,2,3],[4,5,6]]
a[0][0] = 100
print(b)
print()

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())
print()

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods # shallow copy
friend_foods = my_foods[:] # deep copy
my_foods.append('cannoli')
print(my_foods)
print(friend_foods)


