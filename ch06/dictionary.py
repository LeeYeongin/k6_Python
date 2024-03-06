# key값은 unique함
a = { # key, value로 이루어져있음
     'a': 1,
     'b': 2,
     'c': 3
    }
b = [1, 2, 3]
print(f"a type: {type(a)}, b type: {type(b)}")
print(a['b'])
print()

print(f"a: {a}")
# 추가
a['d'] = 4
print(f"추가 후: {a}")

# 수정
a['b'] = 5
print(f"수정 후: {a}")

# 삭제
del a['b']
print(f"삭제 후: {a}")
print()

db = {
        1: ["정원", "A+"],
        2: ["윤정", "A+"],
        3: ["세영", "A+"]
    }

# print(db[4]) ## 오류 KeyError: 4 발생
if 4 in db:
    print(db[4]) # if문으로 오류 발생 방지
print(db.get(4)) ## 오류 발생 X, None 출력
print()

for row in db:
    print(row)
print()

for row in db.items():
    print(row, type(row))
print()

for row in db.items():
    print(row[0],row[1], type(row))
print()

for k,v in db.items():
    print(k,v, type(row))
print()

c = [3, 2, 1]
print(c)
# c.sort() 영구적으로 반영되므로 위험
# print(c)
print(sorted(c), c)
print()

db2 = {
        7: ["정원", "A+"],
        4: ["윤정", "A+"],
        2: ["세영", "A+"]
    }
print(sorted(db2))
print(sorted(db2.items()))
print()

db3 = {
        7: 'C',
        4: 'B',
        2: 'A'
    }
print(sorted(db3.items()))
first = lambda x : x[0]
second = lambda x : x[1]

for row in db3.items():
    print(first(row), second(row))
print()

print(sorted(db3.items(), key=second))
print()

# list 중첩가능
lst = [[1,2,3],[4,5,6]]
lst2 = [db,db2] # 어떤 type이든 중첩가능
print(lst)
print(lst2)
print()

# dict 중첩가능
d1 = {
    'a' : {
        'aa':1,
        'aa1':2
    },
    'b' : [] # dict도 any type이 가능
}
print(d1)
print()

db4 = {}
db4['a'] = list()
db4['a'].append('3')
db4['a'].append('영인')
db4['a'].append('A+')
print(db4)

db4['b'] = list()
db4['b'] = 3 # append를 사용하지 않아 list가 사라지고 숫자 3으로 변함
print(db4)

#------------- 알아두면 좋은 파이썬 ----------------
def add(a,b):
    return a+b
print(add(1, 2))

data = {
    'a':1,
    'b':2
}
print(data)
print(add(**data))
print()

data = {'a':1, 'b':2, 'c':3}
print(data)
data_key={v:k for k, v in data.items()}
print(data_key)
m=[x**2 for x in range(5) if x % 2 == 0]
print(m)
