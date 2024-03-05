from random import randint
print(randint(1,6)) # 1-6사이 수 랜덤하게
print(randint(1,6))
print(randint(1,6)) 

from random import choice
players = ['a',  'b', 'c', 'd', 'e']
first = choice(players) # 랜덤하게 하나 선택
print(first)
second = choice(players)
print(second)
