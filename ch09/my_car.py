from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# 1. 속성값 직접 수정하기
my_new_car.odometer_reading = 23 # 속성이 public이다
my_new_car.read_odometer()
# 2. 메서드를 통해 속성값 수정하기
my_new_car.update_odometer(11)
my_new_car.read_odometer()
my_new_car.increment_odometer(23_500)
my_new_car.read_odometer()