# MySQL 설정

데이터베이스 생성하기
```sql
CREATE DATABASE Security;
```
데이터베이스 유저 생성
```sql
CREATE USER 'yws'@'%' IDENTIFIED BY '********';
```
yws 유저에게 모든 권한 부여
```sql
GRANT ALL PRIVILEGES ON *.* TO 'yws'@'%';
```
즉시 적용
```sql
FLUSH PRIVILEGES;
```
Security 데이터베이스로 이동
```sql
USE Security;
```
회원가입을 위한 테이블 생성
```sql
CREATE TABLE member_info (
  member_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  login_id VARCHAR(40) NOT NULL,
  login_name VARCHAR(20) NOT NULL,
  login_pw VARCHAR(256) NULL,
  insert_date DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (member_id),
  UNIQUE INDEX login_id (login_id)
)
COMMENT='회원'
COLLATE='utf8mb4_general_ci'
;
```
```sql
member_info    = table 이름
```
```sql
member_id      = column 이름 (회원 일련번호)
BIGINT         = 8바이트 정수형. -9223372036854775808 ~ 9223372036854775807
UNSIGNED       = 음수의 범위를 양수로 바꿔주는 것. 0 ~ 18446744073709551614
NOT NULL       = 해당 필드에 NULL 값을 저장할 수 없음(무조건 데이터를 가지고 있어야 함.)
AUTO_INCREMENT = 1부터 시작하며 자동으로 증가
```
```sql
login_id       = column 이름 (로그인 아이디)
VARCHAR(40)    = 가변 문자 필드(문자 데이터), 최대 40글자까지 입력 가능
NOT NULL       = 해당 필드에 NULL 값을 저장할 수 없음
```
```sql
insert_date    = column 이름 (날짜)
DATETIME       = YYYY-MM-DD HH:MM:SS 형식
NOT NULL       = 해당 필드에 NULL 값을 저장할 수 없음.
DEFAULT NOW()  = 기본으로 현재 시간을 저장
```
```sql
PRIMARY KEY (member_id) = 
PRIMARY KEY 제약 조건을 설정하면, 해당 필드는 NOT NULL과 UNIQUE 제약 조건의 특징을 모두 가진다. 
따라서 이 제약 조건이 설정된 필드는 NULL 값을 가질 수 없으며, 또한 중복된 값을 가져서도 안 된다.
이러한 PRIMARY KEY 제약 조건을 기본 키라고 한다.
UNIQUE는 한 테이블의 여러 필드에 설정할 수 있지만, PRIMARY KEY는 테이블당 오직 하나의 필드에만 설정할 수 있다.
이러한 PRIMARY KEY 제약 조건은 테이블의 데이터를 쉽고 빠르게 찾도록 도와주는 역할을 한다.
(유저의 고유 번호는 중복될 수 없고 데이터가 없을 수 없다.)
```
```sql
UNIQUE INDEX login_id (login_id) =
UNIQUE 제약 조건을 설정하면, 해당 필드는 서로 다른 값을 가져야 한다.
즉, 이 제약 조건이 설정된 필드는 중복된 값을 저장할 수 없다.
(사용자 아이디는 중복될 수 없다.)
```
```sql
COMMENT='회원'  = 주석(코멘트)를 달아서 테이블을 조회했을 때 어떤 테이블인지 설명할 수 있음.
```
```sql
COLLATE='utf8mb4_general_ci' = 한글을 사용하기 위한 코드.
```
[DEFAULT 옵션 확인](https://mimah.tistory.com/entry/MySQL-MySQL-8%EC%97%90%EC%84%9C-DATE-default-%ED%98%84%EC%9E%AC-%EB%82%A0%EC%A7%9C)
</br>
</br>
</br>


글을 저장하기 위한 테이블 생성
```sql
CREATE TABLE post_board (
  post_id BIGINT(20) unsigned NOT NULL AUTO_INCREMENT,
  post_content VARCHAR(500) NOT NULL,
  member_id BIGINT(20) unsigned NOT NULL,
  insert_date datetime NOT NULL DEFAULT NOW(),
  PRIMARY KEY (post_id),
  KEY FK_post_board_member_info (member_id),
  CONSTRAINT FK_post_board_member_info FOREIGN KEY (member_id) REFERENCES member_info (member_id)
)
COMMENT='글'
COLLATE='utf8mb4_general_ci'
;
```
```sql
KEY FK_post_board_member_info (member_id),
CONSTRAINT FK_post_board_member_info FOREIGN KEY (member_id) REFERENCES member_info (member_id) = 
post_board 테이블의 member_id 컬럼의 데이터는 member_info 테이블의 member_id 컬럼의 정보를 참조해야 한다.
관계형 데이터베이스에서 다른 테이블의 정보를 참조하는 것을 외래키(Foreign Key)라고 부른다. 예시에서 post_board 테이블은 member_info 테이블을 참조하므로 외래키가 잡혀있다고 표현한다.
```