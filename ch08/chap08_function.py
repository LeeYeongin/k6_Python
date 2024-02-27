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
