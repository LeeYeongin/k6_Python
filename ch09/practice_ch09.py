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


