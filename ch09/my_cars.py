# from modul_name import * ### 잘 사용하지 않음

# 파일을 import하는 경우
import car as c

my_mustang = c.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = c.ElectricCar('nissan', 'leaf', 2024)
print(f"차량 배터리 크기는 {my_leaf.get_descriptive_name()}")

# 여러 클래스 임포트하기
# from car import Car, ElectricCar 

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(f"차량 배터리 크기는 {my_leaf.get_descriptive_name()}")