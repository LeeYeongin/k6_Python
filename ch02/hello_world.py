# 이것만 알면 검색왕 효과적인 구글 검색을 위한 10가지 팁 -> 구글링할때 참고해서 해보기
# python version 3.9.13


print("hello")
name = 'ada lovelace'
print(name.upper()) # 전부 대분자로 변경
print(name.title()) # 문자열의 단어들의 첫 문자를 대문자로 변경

# f-문자열 -> f는 format을 의미. 문자열안에 변수를 사용할때 사용
first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name.title()}!"
print(full_name)

# \n: 줄바꿈, \t: tab 공백
print('language: \nPython\tjava')

# strip(): 공백제거
last_name = ' lovelace '
print(last_name.rstrip()) # 오른쪽 공백제거
print(last_name.lstrip()) # 왼쪽 공백제거
print(last_name.strip()) # 전체 공백 제거

# 접두사 제거 (원하는 접두사 제거)
nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
simple_url = nostarch_url.removeprefix('https://') # strip()처럼 원래 문자열 변경X 이므로 원래 Or 다른 변수에 할당

# 문자열 문법 에러
# message = 'One of python's strengths is its diverse community'
#   File "<stdin>", line 1
#     message = 'One of python's strengths is its diverse community'
#                              ^
# SyntaxError: invalid syntax

# \를 사용하여 오류 해결
message = 'One of python\'s strengths is its diverse community'

# _을 사용하여 읽기 쉽게 숫자 표현 가능
universe_age = 14_000_000_000
print(universe_age) # 그냥 14000000000으로 출력

# 다중 할당 가능
x, y, z = 0, 0, 0

# 상수는 대문자로 선언
MAX_CONNECTIONS = 5000