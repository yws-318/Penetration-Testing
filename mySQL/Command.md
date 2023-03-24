mysql 들어가기(비밀번호)
mysql -u root -p

저장
flush privileges;

데이터베이스, 테이블 확인
SHOW databases;
SHOW tables;

유저, 접속 허용 IP 확인
SELECT user,host FROM mysql.user;
-user
-authentication_string
-plugin
-host

데이터베이스 생성
CEATE DATABASE c318;

데이터베이스 삭제
DROP DATABASE c318;

데이터베이스 변경
USE c318;

유저 만들기
CREATE USER 'yws'@'localhost' IDENTIFIED BY 'password';
- localhost : 내부 네트워크
- %         : 모든 IP 허용

유저 권한 부여
GRANT ALL PRIVILEGES ON *.* TO 'yws'@'localhost';
- *.*      : 모든 데이터베이스의 권한 부여
- energy.* : energy 데이터베이스의 모든 권한 부여
~WITH GRANT OPTION;~

