cars = ['audi', 'bmw','subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 존재를 확인할 때, in 사용(없을 땐 not in)
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) # true
print('pepperoni' in requested_toppings) # flase
print()

# if else 문장
age = 12
if age < 4:
    print('입장료 0$')
elif age < 18:
    print('입장료 25$')
else:
    print('입장료 48$')
print()

# list와 if문
available_toppings = ['mushrooms', 'green peppers', 'pepperoni', 'pineapple']
requested_toppings =  ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('sorry')
    else:
        print(f'Adding {requested_topping}.')
print()

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f'sorry, wd dont\'t have {requested_topping}')
        print(f'Adding {requested_topping}.')
print('finish your pizza')