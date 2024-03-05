# 파이썬의 특수목적 메소드
class Person:
    count = 0 # 클래스 변수
    def __init__(self, name, age, address): # 생성자 역할
        self.name = name ### 인스턴스 변수
        self.age = age
        self.address = address
        self.lst = [10,20,30,40,50,60,70] 
        self.weight = 70 # public(공개) 속성
        self.height = 1.7
        self.__vision = 1.0 # private 속성
        print("{}객체가 생성 되었습니다.".format(self.name))
        Person.count += 1 ### 클래스 변수를 증가
    
    @classmethod # decorator - 자바 용어는 annotation
    def printing(cls):
        print("객체수는 {}".format(cls.count))

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
    
    # 6. __del__ : 프로그램이 끝나면 자동으로 소멸(반환) -> garbage collection
    def __del__(self):
        print("객체 {}이 소멸되었습니다.".format(self.name))
        Person.count -= 1
        
    def show_persion_vision(self):
        print("시력은 {}".format(self.__vision))

Person('guest', 11, 'jeju') # 이 객체를 참조하는 변수가 없으므로 garbage collector대상

new_person = Person('hong', 20, 'busan')
other_person = Person('Kim', 30, 'masan')
other_person2 = Person('Kim', 30, 'busan')   

# 모두 Person객체이므로 count 필드를 공유함 -> count값은 모두 같은값 출력
print(f"{Person.count} 객체가 생성됨") 
print(f"{other_person.count} 객체가 생성됨")
print(f"{new_person.count} 객체가 생성됨")
Person.printing()
new_person.printing()
print()

print(f"Person 객체의 나이는 **{new_person.age:5}**")  # 5칸 안에 나이 찍기
print("객체의 타입은 {}".format(type(new_person)))
print("객체의 타입은 {}".format(isinstance(new_person, Person))) # new_person이 Person class인가?
print("이 사람은 {}".format(new_person.name))
print(f"몸무게는 {new_person.weight}")
# print("시력은 {}".format(new_person.__vision)) -> private 속성이라 바로 사용 불가
new_person.show_persion_vision() # 함수를 사용하여 출력
print()

# 1. __str__
# 모두 동일한 결과 출력
print(str(new_person))
print(new_person.__str__())
print(new_person)
print()

# 2. __len__
my_list = [1,2,3,4]
print(len(my_list))
print(my_list.__len__())

print(f"리스트 길이 {len(new_person)}") # 새로 정의된 len함수 호출
print()

# 3. __eq__ : ==
print(new_person == other_person) # 새로 정의된 __eq__함수 호출 (address를 비교하는 함수)
print(new_person == other_person2) 
print()

# 4. __call__
print(f"체질량은 {new_person()}") # __call__() 함수가 호출
print()

# 5. __getitem__ : 인덱스에 접근할 때 자동으로 호출되는 메서드
print(new_person[0])
print(new_person[1])
print(new_person[2])
print()