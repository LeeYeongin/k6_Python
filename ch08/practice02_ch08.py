from chap08_function2 import build_profile

# 8-12 샌드위치
def making_sandwich(*ingredients):
    print("주문받은 샌드위치 재료입니다: ")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    print()

making_sandwich('빵','햄','양상추')
making_sandwich('빵','계란','양상추','토마토')
making_sandwich('빵','연어','양상추', '올리브', '치즈')

# 8-13 사용자 프로필
my_profile = build_profile('YeongIn','Lee', location='Busan', age='25')
print(my_profile)
print()

# 8-14 자동차
def make_car(maker, model, **info):
    info['maker'] = maker
    info['model'] = model
    return info

car = make_car('subaru', 'outback', color='blue', two_package=True)
print(car)