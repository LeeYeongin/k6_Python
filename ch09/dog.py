class Dog:
    """개를 표현하는 클래스"""
    # 참고: https://codermun-log.tistory.com/73
    # 생성자 
    def __init__(self, name, age): # self: 생성된 객체 자기자신
        """name과 age 속성 초기화"""
        self.name = name # 속성 > 자바의 클래스 field
        self.age = age
        self.price = 100

    def sit(self): # 모든 클래스의 함수는 self를 가지고 있음
        """앉기"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """구르기"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6) # 생성자 호출 > 인스턴스 생성 > __init__() 함수가 자동 호출
my_dog.sit() # self는 실제 사용시 매개변수 따로 입력 X
print(f"개 이름은 {my_dog.name} + {my_dog.price}")
your_dog = Dog('Lucy', 3)
your_dog.sit()
print(f"너의 개는 {your_dog.name}")