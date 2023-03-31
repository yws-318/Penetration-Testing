- **mysql 들어가기(비밀번호)**<br />
mysql -u root -p<br />
<br />

- **저장**<br />
flush privileges;<br />
<br />

- **데이터베이스, 테이블 확인**<br />
SHOW databases;<br />
SHOW tables;<br />
<br />

- **유저, 접속 허용 IP 확인**<br />
SELECT user,host FROM mysql.user;<br />
-user<br />
-authentication_string<br />
-plugin<br />
-host<br />
<br />

- **데이터베이스 생성**<br />
CEATE DATABASE c318;<br />
<br />

- **데이터베이스 삭제**<br />
DROP DATABASE c318;<br />
<br />

- **데이터베이스 변경**<br />
USE c318;<br />
<br />

- **유저 만들기**<br />
CREATE USER 'yws'@'localhost' IDENTIFIED BY 'password';<br />
-localhost : 내부 네트워크<br />
-%         : 모든 IP 허용<br />
<br />

- **유저 권한 부여**<br />
GRANT ALL PRIVILEGES ON \*.\* TO 'yws'@'localhost';<br />
-\*.\*      : 모든 데이터베이스의 권한 부여<br />
-energy.* : energy 데이터베이스의 모든 권한 부여<br />
~WITH GRANT OPTION;~<br />

