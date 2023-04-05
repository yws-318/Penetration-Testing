# DB에 데이터를 넣고 화면에 출력

apache2 시작
```
service apache2 start
```
</br>

test table 안에 있는 내용 확인하기
```sql
$ mysql -uroot -p
mysql> use test;
mysql> select * from test;
```
![tablecontent](https://user-images.githubusercontent.com/106296883/230068023-c17abc7b-0244-48ca-9bd8-0c75b9a2feba.PNG)
</br>
</br>

start.php 파일 수정하기
```
sudo nano start.php
```
</br>

php파일에 데이터베이스 연결, 출력 코드 작성
```php
<?php
$conn = mysqli_connect(
  'localhost', //IP
  '********',  //ID
  '********',  //PW
  'test');     //database name
$sql = "SELECT * FROM test";
$result = mysqli_query($conn, $sql);
$row = mysqli_fetch_array($result);
echo '<h2>'.$row['intnumber'].'</h2>';
echo $row['anything'];

?>
```
</br>

웹 브라우저에서 확인
```
http://localhost/start.php
```
![webcontent](https://user-images.githubusercontent.com/106296883/230068550-c0ff0e26-a32c-460a-be4c-511706eeaaf6.PNG)
