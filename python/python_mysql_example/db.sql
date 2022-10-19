-- Python 프로그램 연동에 사용할 계정 생성
CREATE USER 'kim'@'localhost' IDENTIFIED BY '1234';

-- Python 프로그램 연동에 사용할 데이터베이스 생성.
CREATE DATABASE python_app;

-- 위에서 생성한 계정에 대해 권한 부여
GRANT ALL PRIVILEGES ON python_app.* TO 'kim'@'localhost';




