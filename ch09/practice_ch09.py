# 9-1, 9-2
class Restaurant:
    def __init__(self, name, ctype):
        self.restaurant_name = name
        self.cuisine_type = ctype

    def describe_restaurant(self):
        print(f"restaurant name: {self.restaurant_name}, cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} 문을 열었습니다.")

restaurant = Restaurant("Ganghwaru", "Chinese")
restaurant2 = Restaurant("AAA", "Korean")
restaurant3 = Restaurant("Cury", "India")
print(f"레스토랑 이름과 타입: {restaurant.restaurant_name} {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant.open_restaurant()
print()

# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, name, ctype, flavors):
        super().__init__(name, ctype)
        self.flavors = flavors

    def show_flavors(self):
        print("맛이 {}".format(self.flavors))
        # print(f"맛이 {self.flavors}") # 위와 동일한 방식

ice_cream = IceCreamStand("Italy", "Pizza", "매운맛")
ice_cream.show_flavors()
print()


# 9-3
class User:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def describe_user(self):
        print(f"사용자의 이름은 {self.first_name} {self.last_name}입니다.")
    
    def greet_user(self):
        print(f"어서오세요 {self.first_name}님")

new_user = User("YeongIn", "Lee")
new_user.describe_user()
new_user.greet_user()
print()

# 9-8
class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("사용할 수 있는 권리자 권한은 다음과 같습니다:")
        for p in self.privileges:
            print(f"- {p}")

# 9-7
class Admin(User):
    def __init__(self, first, last, privileges):
        super().__init__(first, last)
        self.privileges = Privileges(privileges)

    # def show_privileges(self):
    #     print("사용할 수 있는 권리자 권한은 다음과 같습니다:")
    #     for p in self.privileges:
    #         print(f"- {p}")
    
    

new_manager = Admin("GilDong","Hong",['can delete post', 'can add post'])
new_manager.greet_user()
# new_manager.show_privileges() -> 9-7 문제
new_manager.privileges.show_privileges() # 9-8 문제

# 9-9는 electric_car.py에 구현
print()

# 9-13
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        num = randint(1,self.sides)
        print(f"주사위의 숫자는 {num}입니다.")

print("[6면체 주사위]")
six_dice = Die()
for i in range(10):
    print(i+1, end=": ")
    six_dice.roll_die()
print()

print("[10면체 주사위]")
ten_dice = Die(10)
for i in range(10):
    print(i+1, end=": ")
    ten_dice.roll_die()
print()

twenty_dice = Die(20)
print("[20면체 주사위]")
for i in range(10):
    print(i+1, end=": ")
    twenty_dice.roll_die()
print()

# 9-14, 9-15
from random import choice

def get_Number(lotto):
    winNumber = []
    for i in range(4):
        winNumber.append(choice(lotto))
    return winNumber

lotto = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d']
win_lotto = get_Number(lotto)
print(f"다음 번호와 일치하면 상금지급: {win_lotto}")
my_ticket = get_Number(lotto)

same = 0
cnt = 0
while same != 4:
    for i in my_ticket:
        if i in win_lotto:
            same += 1
    
    if same != 4:
        same = 0
        my_ticket = get_Number(lotto)

    cnt += 1

print(f"당첨자 티켓: {my_ticket}")
print(cnt)





