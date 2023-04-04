# test db 생성 / test table 생성 후 아무 데이터 넣기

mysql 들어가기
```
$ mysql -uroot -p
```
</br>

데이터베이스 확인
```sql
show databases;
```
</br>

test 데이터베이스 생성
```sql
create database test;
```
![showdb](https://user-images.githubusercontent.com/106296883/229830405-9016f941-5ff9-40e5-bc68-2e7759058d10.PNG)
</br>
</br>

test db 입장
```sql
use test;
```
</br>

table 만들기
```sql
create table test(
    anything varchar(20),
    intnumber int(10)
);
```
</br>

table 확인
```sql
show tables;
```
![showtable](https://user-images.githubusercontent.com/106296883/229830699-430fd6e1-a473-4ca2-84b5-b38e8d008e81.PNG)
</br>
</br>

아무 데이터 넣기
```sql
insert into test (anything, intnumber) value('testdb', 1234);  
```
</br>

데이터 확인하기
```sql
select * from test;
```
![select](https://user-images.githubusercontent.com/106296883/229830831-e01b7d43-03cf-42e8-97a6-2505214996df.PNG)