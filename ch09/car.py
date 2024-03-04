class Car:
    """자동차 클래스"""
    def __init__(self, make, model, year):
        """자동차 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """뜻이 분명하고 깔끔한 이름 반환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """자동차의 주행거리를 출력합니다"""
        print(f"이 차의 주행거리는 {self.odometer_reading}마일 입니다.")

    def update_odometer(self, mileage):
        """
        거리계를 주어진 값으로 설정합니다
        현재 값보다 적은 값을 할당할 수 없습니다.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """거리계 값을 주어진 값만큼 늘립니다"""
        self.odometer_reading += miles
    
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
