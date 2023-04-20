# SQL Injection

SQL Injection 은 POST 데이터에서 데이터베이스를 조회할 수 있는 부분에 데이터베이스를 동작시킬 수 있는 query 문을 주입하여 공격자가 원하는 행동을 유발시킬 수 있는 공격 방법이다.

SQL Injectio 공격을 하려면 우선 SQL에 대해서 알아야 한다.

---

## SQL
database : 엑셀 파일   
table : 엑셀 시트    
column : 열    
row : 행   
</br>

## SELECT

select [컬럼 이름] from [테이블 이름] where [컬럼이름='데이터']
```
select pass from member where id='normaltic'
```
</br>

and = 두 가지 모두 참이어야 참   
or = 두 가지 중 하나라도 참이면 참   

```
select * from member where id='mario' and pass='aaaa'
```
</br>
</br>

## 로그인 인증 과정

식별 =   
많은 데이터 중에서 특정한 데이터를 가려내는 것   
식별 정보 : ID   
유니크해야 함 → 중복되면 x 


인증 =   
그 사람이 맞는지 확인   
인증 정보 : 비밀번호 등등

---
</br>

SQL Injectio 은 SQL 질의문을 삽입하는 공격이다.

sql injection을 해서 얻을 수 있는 것.   
→ 데이터 추출    
→ 인증 우회    
→ 데이터 변조   

우선 수업을 통해서 배웠던 SQL Injectio 공격은 3가지이다.
1. 주석처리를 이용한 기법
2. or 을 이용한 기법
3. union 을 이용한 기법
</br> 
</br> 

하지만 이런 것들로는 충분하지 않다.    
## ❗<span style="color:black"><span style="background-color:red">중요한 것은 서버단에서 입력 데이터를 어떤 sql 구문으로 처리했는지 예상하는 것이다</span>❗ 
우리는 크게 식별과 인증을 <U><span style="font-size:150%"><span style="color:yellow">동시</span></U>에 적용했냐, <U><span style="font-size:150%"><span style="color:yellow">분리</span></U>했냐로 구분하여 생각해볼 수 있다.
</br>
</br>

## 그래도 sql injection 위험에는 둘 다 똑같음.   
뭐가 더 안전한 건 없음. 결국 sql injection 을 막을 수 있는 방법을 적용시켜야 함. 둘 다
</br>
</br>
</br>
</br>



간단하게 예시를 들어보겠다.

## 주석 처리를 이용한 기법
```
ID       : adimin'#   
password : 1234(아무거나)
```

## or 을 이용한 기법
```
ID       : admin'or'1'='1
password : 1234(아무거나)
```

## union 을 이용한 기법
```
select * from member union select '1','2','3','4'
```

이 예시들은 간단하게 설명을 하기 위해서 기록해놓았을 뿐, 결국 식별과 인증을 어떻게 구성했냐를 생각해야 한다.

