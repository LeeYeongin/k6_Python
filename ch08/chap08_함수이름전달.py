# 함수의 매개변수로 함수 전달하기
def ten_times(func):
    for i in range(5):
        func()

def print_hello():
    print("hello")

ten_times(print_hello)

def print_work():
    print('coding')

ten_times(print_work)

# 매개변수가 있는 함수를 함수의 매개변수로 전달하기 
def add(x,y):
    return x + y

def minus(x,y):
    return x - y

def apply_operation(operation, x, y): # map() 함수 역할
    return operation(x,y)

result = apply_operation(add, 4, 3)
result2 = apply_operation(minus, 4, 3)
print(f"add 결과 = {result}, minus 결과 = {result2}")

### map(), filter() 함수 사용
# def power(item):
#     return item * item

# def under_three(item):
#     return item < 3

# 위 함수들을 람다식으로 간단히 작성
# 람다식 관련 참고: https://blockdmask.tistory.com/520
power = lambda x: x*x
under_three = lambda x: x<3

lst = [1,2,3,4,5]
map_list = map(power, lst) # map(함수, 데이터)
print(f"map() 함수 적용결과: {list(map_list)}")

filter_list = filter(under_three, lst) # fliter(함수, 데이터)
print(f"filter() 함수 적용결과: {list(filter_list)}")

