# 위치 인수(size)와 임의의 인수(*toppings)
def make_pizza(size, *toppings): # 매개변수의 * -> 전달받은 인수를 튜플에 모음(받음)
    """주문 내용을 요약합니다."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

make_pizza(16,'pepperoni')
make_pizza(12, 'mushromms','green peppers', 'extra cheese')

def build_profile(first, last, **user_info): # 매개변수의 별 두개(**)를 인식 -> 이름(키) - 값 쌍으로 제한없이 받음
    """사용자에 대해 아는 정보를 전부 딕셔너리에 저장합니다"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princetion',
                             field='physics')

print(user_profile) # 출력: {'location': 'princetion', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}