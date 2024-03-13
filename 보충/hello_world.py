# # 출력
# print("Hello World!")

# # 입력
# # a, b = input().split()
# # a, b= int(a), int(b)
# # print(a + b, a - b, a * b, int(a / b), a % b, sep='\n')
# # print('----------- 입력')

# # 문자열 길이
# # a = input()
# # print(len(a))
# # print('----------- 문자열')

# # list
# a = list()
# b = []
# # print(type(a))
# # print(type(b))
# a.append(1)
# a.append(2)
# a.append(3)
# a.append(4)
# a.append(5)

# print(a)
# print(a[::-1])
# print(a[-1])
# print(a[0:3], a[3:])

# # list
# for i in [1, 2, 3, 4, 5]:
#     print(i)
# print('----------- list')

# # str
# for s in 'abcdef':
#     print(s)
# print('----------- str')

# # tuple
# for i in (1,2,3,4,5):
#     print(i)
# print('----------- tuple')

# for i in range(5):
#     print(i)
# print('----------- range')

# for i in range(1,6):
#     print(i)
# print('----------- range')

# # dict
# d = {1: 'a',
#      2: 'b',
#      3: 'c',
#      4: 'd',
#      5: 'e'}
# for i in d:
#     print(i) # key값만 출력
# print('----------- dict')

# # 조건문
# for i in range(1,6):
#     if i % 2 == 0: # and, or로 여러가지 조건 사용 가능 Ex) i%2==0 and i%3==0
#         print(i, 'even')
#     elif i % 3 == 0:
#         print(i, '3')
#     else: # 예외되는 case가 없도록 else로 처리 
#         print(i, 'odd')
# print('----------- if,elif, else문')
# # F8번: 오류발생 지점으로 바로 이동

# --------------------------------------
# # 백준 1330번
# a, b = input().split()
# a, b = int(a), int(b)

# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')

# --------------------------------------
# # 백준 9498번
# a = input()
# a = int(a)

# if a >= 90:
#     print('A')
# elif 80 <= a:
#     print('B')
# elif 70 <= a:
#     print('C')
# elif 60 <= a:
#     print('D')
# else:
#     print('F')

# --------------------------------------
# # 백준 2739번
# N = input()
# N = int(N)

# for i in range(1,10):
#     print(f"{N} * {i} = {i*N}")

# --------------------------------------
# # 백준 8393번
# N = input()
# N = int(N)
# sum = 0

# for i in range(1,N+1):
#     sum += i
# print(sum)

# --------------------------------------
# # 백준 25314번
# N = input()
# N = int(N)
# rpt = int(N/4)

# for i in range(rpt):
#     print('long', end=' ')
# print('int')

# --------------------------------------
# # 백준 10871번
# N, X = input().split()
# N, X = int(N), int(X)
# value = input().split()

# for i in value:
#     if int(i) < X:
#         print(i, end=" ")

# --------------------------------------
# # 백준 1152번
# s = input()
# result = s.split()
# print(len(result))

# --------------------------------------
# # 백준 10818번
# N = input().split()
# lst = list(map(int, input().split()))
# print(min(lst), max(lst))
# print()

# --------------------------------------
# 백준 10807번
# N = int(input())
# lst = list(map(int, input().split()))
# v = int(input())
# print(lst.count(v))

# --------------------------------------
# 백준 10871
# N, X = input().split()
# N, X = int(N), int(X)
# lst = list(map(int, input().split()))

# for i in lst:
#     if X > i:
#         print(i, end=" ")

# --------------------------------------
# 백준 27866
# s = input()
# i = int(input())
# print(s[i-1])

# --------------------------------------
# 백준 3052 - 나머지
# num = [int(input()) for _ in range(10)]
# mod = []
# for n in num:
#     x = n%42
#     if x not in mod:
#         mod.append(x)

# for n in num:
#     mod.append(n%42)

# 코드2
# data = [int(input())%42 for _ in range(10)]
# print(len(set(data))) # set이 알아서 중복을 제거해줌

# print(len(mod))

# --------------------------------------
# 백준 2675 - 문자열 반복
# N = int(input())
# for _ in range(N):
#     r,s = input().split()
#     for s_split in s:
#         for i in range(int(r)):
#             print(s_split, end="")
#     print()

# --------------------------------------
# 백준 1152 - 단어의 개수
# s  = input().split()
# print(len(s))

# --------------------------------------
# diconary사용하기(아래 두 문제)
# --------------------------------------
# 백준 10815
# N = int(input())
# own_card = list(map(int, input().split()))
# M = int(input())
# tmp = list(map(int, input().split()))

# card = dict()
# for i in tmp:
#     card[i] = 0

# for i in own_card:
#     if i in card:
#         card[i] = 1

# for i in card.values():
#     print(i, end=" ")

# data.get(q,0)

# --------------------------------------
# 백준 14425 - 문자열 집합
# N, M = input().split()
# N, M = int(N), int(M)
# S = [input() for _ in range(N)]
# lst = [input() for _ in range(M)]

# cnt=0
# for st in lst:
#     if st in S:
#         cnt += 1
# print(cnt)

# --------------------------------------
# 백준 2750 - 수 정렬하기
### 교수님 코드
# import sys

# N = int(input())
# # data = sys.stdin.readlines() #EOF - Ctrl + z
# data = [int(d.rstrip()) for d in sys.stdin.readlines()]
# print('\n'.join(str(s) for s in sorted(data)))

### 내 코드
# N = input()
# N = int(N)
# lst = [int(input()) for _ in range(N)]
# lst.sort() # sorted는 return이 있고, list는 변화X(원본 유지). sort는 return X, list자체가 변화(원본 유지 X)
# for n in lst:
#     print(n)

# --------------------------------------
# 백준 2587 - 대표값2
# lst = [int(input()) for _ in range(5)]
# print(int(sum(lst)/5))
# lst.sort()
# print(lst[2])

# --------------------------------------
# 백준 25305 - 커트라인
# N,k = input().split()
# N,k = int(N), int(k)
# lst = list(map(int, input().split()))
# lst.sort(reverse=True)
# print(lst[k-1])

# --------------------------------------
# 백준 7785 - 회사에 있는 사람
# import sys
# N = int(input())
# lst = [int(d.rstrip()) for d in sys.stdin.readlines()]
# print('\n'.join(str(s) for s in sorted(lst)))

# --------------------------------------
# 백준 7785 - 회사에 있는 사람 (dict)
# N = int(input())
# log_lst = dict()
# for i in range(N):
#     name, log = input().split()
#     log_lst[name] = log

# in_company = [k for k, v in log_lst.items() if v == 'enter']
# print('\n'.join(person for person in in_company))


# 10988 팰린드롬
# word = input()
# print("1" if word == word[::-1] else "0") # 단어 뒤집어서 일치하는지 확인하기

# 1157 단어공부
# from collections import Counter
# most_common: n번째 까지 가장 많이 나온 요소를 출력(몇개인지 개수도 count)
# print(Counter('hello world').most_common(1)[0][0])

# import string
# print(string.digits)
# print(string.ascii_lowercase)

# s = 'hello world'.lower()
# C = {l:s.count(l) for l in string.digits + string.ascii_lowercase}
# print(C)
# print(sorted(C.items(), key = lambda x: x[1], reverse=True)[0][0])

# 1316 그룹단어 체커
# 2738 행렬 덧셈
# 2566 최댓값
# 10798 세로읽기