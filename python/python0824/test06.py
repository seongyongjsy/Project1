# 파일 입출력
# open(): 파일 열기 함수
# 파이썬 프로그램에서 다루기 위해 파일을 지정하고 여는 작업을 수행
# 파일 경로 및 파일명과 모드를 지정해서 객체로 생성해줌
f = open(r"c:\Workspace\python0824\files\test01.txt", "wt")
# f = open(r"c:\Workspace\python0824\files\test01.txt", "at")
# f = open(r"c:\Workspace\python0824\files\test01.txt", "rt")

#2. read(), write(), ...: 파일 작업 함수
# 연 파일을 작업하는 단계
f.write("새 파일 작성 테스트!\n")
f.write("내용 추가!")
# print(f.read()) # 파일 내 모든 내용을 읽는 함수
# print(f.readline(), end="") # 한 줄 읽는 함수
# print(f.readline(), end="") # 반복해서 실행 시 다음 줄을 계속해서 읽음
# print(f.readline(), end="")
print(f.readlines())  # 각 줄을 목록으로 묶어서 읽는 함수

# 3. close(): 파일 작업에 사용한 자원을 운영체제에 반납하는 단계
# 파일 작업이 완료됐다는 것을 수동으로 알리는 의미
f.close()

# 모드
# r: 읽기 모드, 파일을 불러와서 내용을 조회하는 용도로 사용
# w: 쓰기 모드, 새 파일을 작성 또는 덮어씌우기 하는 용도로 사용
# a: 추가 모드, 기존 내용에 새 내용을 덧붙이는 용도로 사용
# x: 쓰기 모드로 동작하되, 새 파일 작성만 가능
# t: 텍스트 파일 형식으로 사용
# b: 바이너리 파일 형식으로 사용
