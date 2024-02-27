bicycles = ['trek', 'cannondale', 'readline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[3])
print(bicycles[-1]) # 마지막 값으로 접근
print(bicycles[-2]) # 뒤에서부터 인덱스 접근 (뒤에서 두번째)
message = f"bicycles was a {bicycles[2].title()}!!!"
print(message)

motorcycles =  ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('GM') # list의 맨 뒤에 추가
print(motorcycles)
motorcycles.insert(1, 'Samcheonri') # index 1번째 자리에 삽입
print(motorcycles)
del motorcycles[0] # 맨처음 요소가 삭제됨 (함수 형태 X)
print(motorcycles)
popped_mortor = motorcycles.pop() # 맨위(=마지막 입력/요소)가 제거 + 제거된 해당 요소 반환
print(motorcycles)
print(popped_mortor)
print(f'the last owned motor was a {popped_mortor.title()}.')
popped_mortor = motorcycles.pop(1) # 원하는 위치의 요소 제거 + 제거된 해당 요소 반환
print(motorcycles)
print(popped_mortor)
motorcycles.append('ducati')
motorcycles.remove('ducati') # 제할 요소의 위치를 모르고 값만 알고 있는 경우 사용. 같은 값이 두가지 있는경우 앞의 요소부터 삭제(삭제할 만큼 remove수행해야함)
print(motorcycles)
print()

cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort() # 알파벳 순서로 정렬(영구히)
# cars.sort(reverse=True) # 알파벳 역순으로 정렬
print(sorted(cars)) # 임시로 알파벳 순서로 정렬
print(sorted(cars, reverse=True)) # 임시로 알파벳 역순으로 정렬
print(cars)
print(len(cars)) # list의 길이(요소 수)
print()
# print(cars[4]) 없는 index이므로 오류 발생 -> 마지막 접근시 -1을 사용하는 것이 더 좋음 
#   Traceback (most recent call last):
#       File "c:\k6_programming\python_work\list.py", line 40, in <module>
#       print(cars[4])
#   IndexError: list index out of range

for car in cars: # 확장형 for문
    print(car)
    print(f"my car is a {car}") # 들여쓰기로 같은 블록임을 구분
print("리스트 출력 완료")

for car2 in cars:
    print('my car\n')
    for c2 in cars:
        print()

print('for문 종료')
