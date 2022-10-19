#문자열 포매팅
#1. 치환 연산자(%)
from turtle import title


year_str = "올해는 %d년입니다." % 2022
print(year_str)
today_str = "오늘은 %d월 %d일입니다" %( 8, 16)
print(today_str)

test_title = "중간고사"
avg_score = 78.9
print("<< %s 결과 >> - 평균: %.1f점" % (test_title, avg_score))
print("<<", test_title, "결과 >> - 평균", avg_score, " 점")

print("="* 50)
# %? => 치환 명세
# %d => decimal, 십진수 정수
# %s => string, 문자열
# %f => float, 실수
# %% => % 기호

# 2. format()
year_str = "올해는 {}년입니다.".format(2022)
print(year_str)
today_str = "오늘은 {0}월 {1}일입니다.".format(8, 16)
print(today_str)
test_title = "기말고사"
avg_score = 67.89
print("<< {0} 결과 >> - 평균 : {1}점".format(test_title, avg_score))
print("<< {0:^10} 결과 >> - 평균 : {1:.8}점".format(test_title, avg_score))
positive_value : 1.23
negative_value : -1.23
print("{0:+} {0:-} {0: }".format(positive_value))
print("{0:+} {0:-} {0: }".format(negative_value))

print("=" * 50)

# 3. f-string
this_year = 2022
year_str = f"올해는 {this_year}년입니다."
print(year_str)
year_str = f"내년은 {this_year+1}년입니다."
print(year_str)
month = 8
day = 16
today_str = f"오늘은 {month}월 {day}입니다."
print(today_str)
test_title = "모의고사"
avg_score = 89.012345
print(f"<<{test_title} 결과 >> - 평균: {avg_score}점")
print(f"<<{test_title:^10} 결과 >> - 평균: {avg_score:.4}점")
score_list = {80.4, 77.6 , 92.1}
print(f"최고 점수: {max(score_list)}, 최저 점수: {min(score_list)}")


student_name = "홍길동"
student_age = 20
student_score = 30
print("student_name=", student_name, "student_age=",student_age ,"student_score =",student_score  )
print(f"{student_name=}, {student_age=},{student_score =}")
