from datetime import datetime as dt
import datetime

today = dt.strptime('2021-03-15', '%Y-%m-%d') # 문자열을 datetime.datetime type으로 변경
print(today, type(today), type('2021-03-15'))
print(today + datetime.timedelta(days=3)) # 날짜 계산이 쉬워짐
print(datetime.datetime(2024, 3, 14))