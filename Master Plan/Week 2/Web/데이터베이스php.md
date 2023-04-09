# 데이터베이스.php 설정

/var/www/html 디렉토리로 들어가서   
inc 폴더 생성 후 db.php 이름으로 저장

## db.php
```php
<?php
function db_get_pdo()
{
    $host = 'localhost';
    $port = '3306';
    $dbname = 'Security';
    $charset = 'utf8';
    $username = 'yang';
    $db_pw = "********";
    $dsn = "mysql:host=$host;port=$port;dbname=$dbname;charset=$charset";
    $pdo = new PDO($dsn, $username, $db_pw);
    return $pdo;
}

function db_select($query, $param=array()){
    $pdo = db_get_pdo();
    try {
        $st = $pdo->prepare($query);
        $st->execute($param);
        $result =$st->fetchAll(PDO::FETCH_ASSOC);
        $pdo = null;
        return $result;
    } catch (PDOException $ex) {
        return false;
    } finally {
        $pdo = null;
    }
}

function db_insert($query, $param = array())
{
    $pdo = db_get_pdo();
    try {
        $st = $pdo->prepare($query);
        $result = $st->execute($param);
        $last_id = $pdo->lastInsertId();
        $pdo = null;
        if ($result) {
            return $last_id;
        } else {
            return false;
        }
    } catch (PDOException $ex) {
        return false;
    } finally {
        $pdo = null;
    }
}

function db_update_delete($query, $param = array())
{
    $pdo = db_get_pdo();
    try {
        $st = $pdo->prepare($query);
        $result = $st->execute($param);
        $pdo = null;
        return $result;
    } catch (PDOException $ex) {
        return false;
    } finally {
        $pdo = null;
    }
}
```

## 코드 설명
---
# function db_get_pdo()
PHP에서 MySQL 데이터베이스에 접속하기 위한 코드
```php
function db_get_pdo()
{
    $host = 'localhost';
    $port = '3306';
    $dbname = 'Security';
    $charset = 'utf8';
    $username = 'yang';
    $db_pw = "********";
    $dsn = "mysql:host=$host;port=$port;dbname=$dbname;charset=$charset";
    $pdo = new PDO($dsn, $username, $db_pw);
    return $pdo;
}
```
```php
host     = 데이터베이스 서버의 주소
port     = 데이터베이스 서버의 포트.
dbname   = 데이터베이스 이름
charset  = 인코딩 방법. 대부분 utf8을 사용
username = 데이터베이스 사용자 이름
db_pw    = 데이터베이스 사용자 비밀번호
dsn      = 데이터베이스 관련 정보를 바탕으로 만든 데이터베이스 연결 문자열
PDO      = PDO(***) 객체는 dsn, username, db_pw 를 파라미터로 받아서 데이터베이스에 실제로 연결하는 역할을 한다.

PDO 외에도 mysql_ 계열의 함수가 있으나 PHP 7 이상에서는 사용 권장 안함이 되었으므로 사용하지 말자. 
```
</br>
</br>

# function db_select()
PHP에서 MySQL 데이터베이스에서 데이터를 가져오기 위한 코드
```php
function db_select($query, $param=array()){
    $pdo = db_get_pdo();
    try {
        $st = $pdo->prepare($query);
        $st->execute($param);
        $result =$st->fetchAll(PDO::FETCH_ASSOC);
        $pdo = null;
        return $result;
    } catch (PDOException $ex) {
        return false;
    } finally {
        $pdo = null;
    }
}
```
```php
$pdo = db_get_pdo();


mysql에 접속하는 객체
```
```php
$st = $pdo->prepare($query);


쿼리문을 준비해서 pdo에 실행시킬 준비를 하는 것이 $st 객체라는 의미.

일반적으로 "->" 연산자는 PHP에서 개체의 멤버에 액세스하는 데 사용됩니다.
즉, 연산자의 오른쪽에 있는 것이, 연산자의 왼쪽에 있는 변수로 인스턴스화되어 하나의 객체 구성원이 된다. 결국 객체($pdo)의 메서드 및 속성에 액세스하는 데 사용한다.

$query 에 저장된 SQL 쿼리문을 기반으로 $st 명령문을 준비한다.
PDO는 prepare를 사용하여 쿼리의 모든 사용자 입력이 적절하게 escape되고 SQL Injection을 방지한다.

StatementT($st) 객체는 실제로 쿼리를 실행하는 역할이다. 
pdo 객체에서 쿼리를 세팅하면서 statement 객체 $st 를 리턴받는다

조금 더 구체적으로 말하면 prepare statement라고 해서 쿼리 문자열을 직접 만들어내는 대신 플레이스 홀더(? 혹은 :이름)를 통해 쿼리에 파라미터를 전달하는 객체다.
프리페어 스테이트먼트(prepare statement)는 플레이스 홀더를 통해 전달된 파라미터들의 SQL Injection을 방지하는 역할을 한다.
```
```php
$st->excute($param);


쿼리를 실행한다.
```
```php
$st->fetchAll(PDO::FETCH_ASSOC);


실행한 데이터 전부를 가지고 온다.

fetchAll 은 데이터를 전부 가지고 오는 메소드이다.

PDO::FETCH_ASSOC = key값으로 접근 가능, 
                   져온 데이터는 $row['id']와 같은 식으로 사용한다, 
                   컬럼명이 키인 연관배열 반환
```
```php
$pdo = null;


객체를 null로 초기화해야 데이터베이스 연결이 끊긴다.
```
```php
finally {
    $pdo = null;
}


쿼리가 실패하거나 다른 문제가 생기더라도 데이터베이스와의 연결을 끊는다.

연결을 제대로 끊어주지 않으면 데이터베이스 연결이 무한대로 늘어나서 성능에 영향을 미치거나 too many connections 오류를 맞이할 수도 있으므로 반드시 쿼리를 실행하고 나면 연결을 끊어야 한다. 
finally는 오류가 발생해도 실행되는 구문이므로 쿼리의 성공/실패 여부와 관계없이 연결이 끊김을 보장할 수 있다.
```
</br>
</br>

## db_select 함수 사용법
파라미터가 없는 경우 db_select(쿼리 문자열); 형태로 사용한다.
```php
db_select("select * from tbl_person");
```

쿼리에 전달할 파라미터가 있는 경우 db_select(쿼리 문자열, array(파라미터들)) 형식으로 사용한다.
```php
db_select("select * from tbl_person where person_id = ?", array(1))
```
```php
db_select("select * from tbl_person where person_id = :person_id", array('person_id' => 1))
```
</br>
</br>
쿼리에 파라미터를 전달하는 방법은 두개가 있다.

첫번째로는 쿼리 문자열 안에 ? 로 넣는 것이다. 이 때 파라미터 배열은 순차 배열로 전달하며 ? 의 갯수만큼 순서대로 적용된다.
```php
db_select("select * from tbl_person where person_id = ?", array(1))
```
?가 배열의 값 1로 대체되었다. 위 구문은 아래와 같은 쿼리를 실행한다.
```sql
select * from tbl_person where person_id = 1
```
두번째는 쿼리 문자열 안에 :키 로 넣을 수 있다. 파라미터 배열은 연관 배열로 전달하며 각 키에 바인딩된다.
```php
db_select("select * from tbl_person where person_id = :person_id", array('person_id' => 1))
```
위 구문은 아래와 같은 쿼리를 실행한다.
```sql
select * from tbl_person where person_id = 1
```

# function db_insert()

PHP에서 MySQL 데이터베이스에서 데이터를 입력하기 위한 코드이다.
```php
function db_insert($query, $param = array())
{
    $pdo = db_get_pdo();
    try {
        $st = $pdo->prepare($query);
        $result = $st->execute($param);
        $last_id = $pdo->lastInsertId();
        $pdo = null;
        if ($result) {
            return $last_id;
        } else {
            return false;
        }
    } catch (PDOException $ex) {
        return false;
    } finally {
        $pdo = null;
    }
}
```

\$pdo->lastInsertId() 메소드는 자동으로 설정되는 PK 를 가지고 온다.
```php
$last_id = $pdo->lastInsertId();
```
db_insert 함수는 성공할 경우 PK 를, 실패할 경우 false 를 반환하므로 === false 체크 후 사용하면 된다.
</br>
</br>

```php
if ($result) {
    return $last_id;
} else {
    return false;
}


if($result)는 excute 작업이 성공했는지 여부를 확인하는 것이다.
$result 가 True 면 excute 작업에 성공하고 $pdo 객체의 lastInsertID() 메서드를 사용해서 마지막으로 삽입된 행의 ID를 반환한다. 이 ID는 $last_id 변수에 저장된다.

$result 가 False 면 excute 작업에 실패하고 false 를 반환한다.
```
```php
catch (PDOException $ex) {
    return false;
} finally {
    $pdo = null;
}


catch, finally 는 데이터베이스 excute 작업을 실행할 때 발생할 수 있는 예외를 처리하는 구문이다.

try 를 실행하는 동안 "PDOException" 유형의 예외가 발생하면 catch 가 실행된다.
이 경우 함수는 데이터베이스 excute 작업이 실패했다는 것을 나타내는 false 를 반환한다.

finally 는 예외 발생 여부에 관계없이 try, catch 가 끝나면 무조건 실행되서 데이터베이스와의 연결을 끊는다.
```
</br>
</br>
</br>

# function db_update_delete()

PHP에서 MySQL 데이터베이스에서 데이터를 수정 혹은 삭제하기 위한 코드

```php
function db_update_delete($query, $param = array())
{
    $pdo = db_get_pdo();
    try {
        $st = $pdo->prepare($query);
        $result = $st->execute($param);
        $pdo = null;
        return $result;
    } catch (PDOException $ex) {
        return false;
    } finally {
        $pdo = null;
    }
}
```
수정 / 삭제는 각자 쿼리문은 다르지만 php에서 처리하는 부분은 동일하다. 따라서 하나의 함수 db_update_delete 에서 처리한다.

수정 / 삭제는 특별히 리턴할 값이 없기 때문에 db_update_delete 함수는 성공/실패 여부를 반환한다.
</br>
</br>
</br>

# chatGPT 

chatGPT에게 db.php 파일을 refactored 해달라고 했더니 이런 코드를 주었다.
```php
function db_execute_query($query, $param = array()) {
    $pdo = db_get_pdo();
    try {
        $st = $pdo->prepare($query);
        $result = $st->execute($param);
        $pdo = null;
        return $result;
    } catch (PDOException $ex) {
        return false;
    } finally {
        $pdo = null;
    }
}

function db_select($query, $param = array()) {
    $pdo = db_get_pdo();
    try {
        $st = $pdo->prepare($query);
        $st->execute($param);
        $result = $st->fetchAll(PDO::FETCH_ASSOC);
        $pdo = null;
        return $result;
    } catch (PDOException $ex) {
        return false;
    } finally {
        $pdo = null;
    }
}

function db_insert($query, $param = array()) {
    if (db_execute_query($query, $param)) {
        $pdo = db_get_pdo();
        $last_id = $pdo->lastInsertId();
        $pdo = null;
        return $last_id;
    } else {
        return false;
    }
}

function db_update_delete($query, $param = array()) {
    return db_execute_query($query, $param);
}
```