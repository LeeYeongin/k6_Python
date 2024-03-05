# 파이썬의 특수목적 메소드
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.lst = [10,20,30,40,50,60,70] 
        self.weight = 70 # public(공개) 속성
        self.height = 1.7
        self.__vision = 1.0 # private 속성

    def __str__(self): # Person은 객체 출력시 필요한 것은 스트링
        return "{}\t{}\t{}".format(self.name, self.age, self.address)
    
    def __len__(self):
        return len(self.lst) + 1
    
    def __eq__(self, other):
        return self.address == other.address
    
    def __call__(self): # 객체를 호출해주는 메소드
        return self.weight / self.height * self.height
    
    def __getitem__(self, index):
        print("__getitem__ 메서드 호출")
        return self.lst[index]
        
    def show_persion_vision(self):
        print("시력은 {}".format(self.__vision))

new_person = Person('hong', 20, 'busan')
other_person = Person('Kim', 30, 'masan')
other_person2 = Person('Kim', 30, 'busan')

print("이 사람은 {}".format(new_person.name))
print(f"몸무게는 {new_person.weight}")
# print("시력은 {}".format(new_person.__vision)) -> private 속성이라 바로 사용 불가
new_person.show_persion_vision() # 함수를 사용하여 출력

# 1. __str__
# 모두 동일한 결과 출력
print(str(new_person))
print(new_person.__str__())
print(new_person)

# 2. __len__
my_list = [1,2,3,4]
print(len(my_list))
print(my_list.__len__())

print(f"리스트 길이 {len(new_person)}") # 새로 정의된 len함수 호출

# 3. __eq__ : ==
print(new_person == other_person) # 새로 정의된 __eq__함수 호출 (address를 비교하는 함수)
print(new_person == other_person2) 

# 4. __call__
print(f"체질량은 {new_person()}") # __call__() 함수가 호출

# 5. __getitem__ : 인덱스에 접근할 때 자동으로 호출되는 메서드
print(new_person[0])
print(new_person[1])
print(new_person[2])