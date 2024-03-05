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

class Battery:
    """배터리"""
    def __init__(self, battery_size=00): # battery가 0이면 전기차가 아님을 의미
        """배터리 속성을 초기화합니다"""
        self.battery_size = battery_size

    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력합니다"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """이 배터리로 주행할 수 있는 거리를 알려줍니다"""
        if self.battery_size <= 40:
            range = 150
        elif self.battery_size >= 65:
            range = 255

        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    """전기차에만 해당하는 특징을 정의합니다"""
    def __init__(self, make, model, year, large_battery=Battery()):
        """
        부모 클래스의 속성을 초기화합니다
        그리고 전기차에만 해당하는 속성을 초기화합니다
        """
        super().__init__(make, model, year)
        self.battery = large_battery

    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력합니다"""
        return f"This car has a {self.battery.battery_size}-kWh battery."

    def get_descriptive_name(self):
        print(super().get_descriptive_name())
        # print(f"차량 배터리 크기는 {self.battery.battery_size}")
        return self.battery.battery_size