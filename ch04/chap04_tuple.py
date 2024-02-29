dimensions =  (10, 20)
# dimensions[0] = 30
print(dimensions)
for dimension in dimensions:
    print(dimension)

dimensions = (200, 50) # -> 얼마든지 재정의하여 사용가능

tuple = 10,20,30,40 # 아무것도(ex.[],{}) 표시하지 않으면 튜플로 간주
print(tuple)  # (10, 20, 30, 40)
print(type(tuple)) # <class 'tuple'>

x,y = 11,22
y,x = x,y # x,y값을 쉽게 바꿀 수 있음
print(x) # 22
print(y) # 11

def test():
    return (10,20)

a,b = test() # tuple값을 리턴
print(f"a={a}, b={b}")
lst = ['a', 'b', 'c', 'd']

# enumerate: tuple을 return해줌
for i, value in enumerate(lst):
    print(f"i = {i}, value = {value}") # 인덱스, 인덱스에 해당하는 값


