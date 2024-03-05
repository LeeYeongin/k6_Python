class Shape:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height # private 변수

    # getter, setter를 정의하는데 decorator 사용
    @property # decorator for getter
    def get_base(self):
        return self.__base
    
    @property # decorator for getter
    def get_height(self):
        return self.height
    
    @height.setter
    def height(self, value):
        self.height=value


def get_data():
    return 1,2,3

_,a,b = get_data() # _으로 첫번째 return값을 무시

a = [1,2,3]
b = [11,22,33]
mylist = [*a, *b] # 병합
print(mylist)

c = ['a','b']
z = zip(a,c)
print(list(z))

s = Shape(10, 150)
print(s.get_base())
print(s.get_height())
# s.height(80)
# print(s.get_height())

