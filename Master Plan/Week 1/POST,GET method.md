# POST method

post 방식의 실행 코드
```php
<form method="post">
    name : <input type="text" name="name" />
    age : <input type="text" name="age" />
    <input type="submit" />
</form>

<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $age = $_POST['age'];

    echo "name is $name, age is $age";
}
?>
```
</br>

![post](https://user-images.githubusercontent.com/106296883/229533138-01832263-ffb9-41f5-ac22-cd880c16dfa1.PNG)
</br>
</br>
</br>

# GET method

get 방식의 실행 코드
```php
<?php

$name = $_GET['name'];
$age = $_GET['age'];

echo "name is $name, age is $age";
?>
```
</br>

GET방식은 url에 데이터를 담아 이동하기 때문에 url을 수정하면 정보를 바꿀 수 있다.   

localhost/start.php<u>?name=yws&age=22   

<u>**?name=yws&age=22**

![get](https://user-images.githubusercontent.com/106296883/229534400-69d8eadf-30a3-48fa-b547-5379b127bb4d.PNG)
