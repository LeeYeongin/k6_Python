n = 0
b_N = True

# while문 사용시 무한루프에 빠지지 않도록 주의하기!
while b_N:
    n += 1
    if n == 3:
        continue # 밑으로 코드 진행 X, 위로 다시 이동
    if n == 5:
        # b_N = False  
        break # while문 탈출
    print(n)
print()

lst=[i for i in range(10)]
print(lst)
print()

a= [1,2,3]
b =[]
N = len(a)

# for i in range(N):
#     p = a.pop()
#     b.append(p)

# while True:
#     # if a == []:
#     #     break
#     if not a: break
#     p = a.pop()
#     b.append(p)

while a:
    p = a.pop()
    b.append(p)

print(a, b)
print()

a=[1,2,3]
a.remove(2)
print(a)
print()

d1 = {}
print("값을 입력해주세요(띄어쓰기로 구분): ", end=" ")
d1['영인'] = list(map(int, input().split()))
print(d1)

