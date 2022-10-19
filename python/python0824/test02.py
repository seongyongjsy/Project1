# date, time, datetime 모듈
import imp
import time
# from unittest import result
print(time.time())  # 현재 시간을 epoch 시간으로 나타내는 함수

# 프로그램 동작 시간 체크 예제
def make_list_by_loop():
    """반복문을 통해서 10만개의 요소를 가지는 리스트 생성 함수"""
        result = []
        for i in range(100000):
            result.append(i)
        return result
    
    def make_list_by_comprehension():
        """컴프리헨션을 이용해서 100만개의 요소를 가지는 리스트 생성 함수"""
        return[i for i in range(100000)]
# start = time.time() # 프로그램 시작 시간(초) 기록
# make_list_by_comprehension()    # 동작 시간을 측정할 코드
# end = time.time()   # 프로그램 종료 시간(초) 기록
# print("동작 시간:", end-start)

print(time.ctime())     # 현재 시간을 문자열로 구함(영어 어순)
print(time.localtime()) # 현재 시간을 struct_time 객체로 구함
today = time.localtime()
print("%d년 %d월 %d일" % (today.tm_year), today.tm_mon, today.tm_mday)
print("%d시 %d분 %d초" % (today.tm_hour, today.tm_min, today.tm_sec))
weekdays = ["월", "화", "수", "목", "금", "토", "일"]
print("오늘은 %s요일입니다."% weekdays[today.tm_wday])

print(time.gmtime())  # 표준 시간대(gmt+00)에 따른 현재 시간 구하는 함수
print(time.localtime(3600))  # epoch 시간을 입력해서 시간 생성 가능
print(time.gmtime(6000))  # epoch 시간을 입력해서 시간 생성 가능
print(time.struct_time([2022, 8, 24, 11, 39, 0, 2, 236, 0]))
print(time.strptime("2022 8 24 11 45 30", "%Y %m %d %H %M %S"))

# print("?")
# time.sleep(3.5) # 프로그램의 실행을 일시중지하는 함수
# print("!")
# for i in range(5):
#     print(5 - i)
#     time.sleep(1)

print("\n", "-"*50, "\n")

import datetime
print(datetime.datetime(2022, 8, 24))   # datetime 객체 생성
today = datetime.datetime.now() # 현재 날짜시간 개게를 생성해주는 함수
print(today)
print("%d년 %d월 %d일" % (today.year, today.month, today.day))
print("%d시 %d분 %d초" % (today.hour, today.minute, today.second))

print(datetime.date(2023, 8, 24)) # date 객체 생성
print(datetime.time(12, 34, 56)) # time 객체 생성
print(datetime.datetime(2022, 8, 24)) # 날짜시간 정보를 가지는 datetime 객체 생성

print(today.replace(year=2023, month=12, day=25))  # 날짜시간 정보를 바꾸는 함수

print("\n", "-"*50, "\n")

# calendar
import calendar
calendar.prcal(12023)   # 특정 년도의 달력을 즉시 출력하는 함수
this_year_str = calendar.calendar(2022) # 특정 년도의 달력을 문자열로 반환하는 함수
print(this_year_str)

calendar.prmonth(2022, 8) #특정 년, 월의 달력을 즉시 출력하는 함수
this_month_str = calendar.month(2022, 8) # 특정 년, 월의 달력을 문자열로 반환하는 함수
print(this_month_str)

print(calendar.isleap(2020))

print("\n", "-"*50, "\n")

# sys, os
import sys
# sys.exit(0)  # 프로그램을 종료하는 함수
sys.path # 모듈을 찾는 경로를 저장한 목록
print(sys.version)   # 현재 설치된 파이썬 버전
print(sys.platform)  # 현재 설치된 파이썬이 어떤 운영체제(플랫폼)에 최적화되어 있는지

import os
file_path = print(os.path.abspath(__file__)) #  절대 경로(C드라이브\...)를 구해주는 함수
print(file_path)   
print(os.path.isfile(file_path))    # 문자열이 파일 경로를 나타내는지 검사
print(os.path.isdir(file_path))     # 문자열이 폴더 경로를 나타내는지 검사
something_path = r"c:\abcd\efg"
print(os.path.exists(something_path)) # 경로가 실제로 존재하는지 검사

