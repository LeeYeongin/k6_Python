def greet_user(username): # username은 String -> String은 immutable
    """인사말""" # 독스트링: 함수가 수행하는 작업 설명
    print(f"hello, {username.title()}")
    username = 'kim'

input_name = 'jessei'
greet_user(input_name) # 함수호출
input_name = 'kim' # 값이 변경이 아니라 변수를 다시 설정(위의 input_name과는 다른 새로운 변수 -> id값이 다름)
print(input_name)

# 함수에 대한 설명 독스트링(docstring) 출력
help(greet_user)
print(greet_user.__doc__) 
print()

# 인수 순서가 매개변수 순서와 일치하는지 확인 필수!
def describe_pet(pet_name, animal_type = 'dog'): # defult parameter는 항상 마지막에
                                                 # (호출시 지정하지 않으면 자동으로 정해진 default값 할당)
    """반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet() -> TypeError: describe_pet() missing 1 required positional argument: 'pet_name'오류 발생
describe_pet('harry')
describe_pet(pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster') # 키워드 인수를 사용하면 인수 순서 상관 X
print()

def get_formatted_name(first_name, last_name, middle_name=''):
    """실제 이름을 깔끔한 형식으로 반환합니다."""
    if middle_name: # 빈스트링이면 False로 간주
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'hooker')
print(musician)
print()

while True:
    print("\n print your name")
    f_name = input("first name을 입력해주세요: ")
    if f_name == 'q':
        break
    l_name = input("last name을 입력해주세요: ")
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nhello, {formatted_name}!")

#-------------------------------------------------------------
# Immutable : 숫자(number), 문자열(string), 튜플(tuple)
# Mutable : 리스트(list), 딕셔너리(dictionary)
# 참고: https://ledgku.tistory.com/54

# p.210~211
def print_models(unprinted_designs, completed_models): # 리스트가 parameter면 변경가능(mutable)
    """
    남은게 없을 때까지 디자인을 출력합니다
    출력이 끝난 디자인은 completed_models 리스트로 이동합니다
    """
    while unprinted_designs: # 빈 리스트이면 false
        current_design = unprinted_designs.pop() # 한개씩 삭제
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_modles):
    """출력된 모델을 모두 표시합니다"""
    print("\nThe following models have been printed:")
    for completed_model in completed_modles:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_modles = []

print_models(unprinted_designs, completed_modles)
show_completed_models(completed_modles)
print()

def modify_string(s): # string은 immutable하므로 변경 불가
    ### immutable 변수는 튜플, 숫자, 스트링, 불리언이 있음
    s = s + " world" # 변수 s는 원래 변수가 가리키는 주소와 다름
    print(s)

st = "hello"
modify_string(st)
print(st) # 출력 결과가 hello로 변경되지 않음을 볼 수 있음

# 리스트를 수정하지 못하게 하기
lst = [1,2,3]
lst_two = lst[:] # 슬라이싱: 사본을 전달(deep copy?)
print(lst_two) # [1, 2, 3]
lst.append(4)
print(lst) # [1, 2, 3, 4]
print(lst_two) # [1, 2, 3]

lst2=lst # shallow copy(같은 주소를 가리킴)
lst2.append(5)
print(lst2) # [1, 2, 3, 4, 5]
print(lst) # [1, 2, 3, 4, 5]