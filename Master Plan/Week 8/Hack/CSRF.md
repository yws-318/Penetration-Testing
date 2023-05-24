# CSRF

CSRF(Cross Site Request Forgery)   
웹 어플리케이션 취약점 중 하나로 인터넷 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 만드는 공격

CSRF 공격이 이루어지려면 다음 조건이 만족되어야 한다.
```   
1. 위조 요청을 전송하는 서비스에 희생자가 로그인 상태
2. 희생자가 해커가 만든 피싱 사이트에 접속
```
의도하지 않았던 요청을 서버에 보내는 것.  
-> 피해자의 세션을 활용함.

CSRF는 모든 요청에서 발생한다.

그만큼 CSRF 공격이 많이 일어남.

로그인을 한 상태로! 해당 링크를 클릭하면 비밀번호가 바뀌게 되어버림.

http://~~~.com/?passwd=1234&confirm=1234&submit=submit

---

# CSRF 방법

## [1] GET 방식을 통해서

Burp suite → Repeater → Change Request method를 통해서    
POST 방식을 GET 방식으로 바꿈.

그러면 쉬워진다

URL
</br>
</br>

## [2] POST method만 허용될 경우

CSRF vs XSS 차이.   

CSRF = 피해자가 의도치 않게 어떤 임의의 요청을 서버에 날리게 만드는 것이다.   
피해자가 자신의 의도와는 다르게, 자신도 모르게 서버로 임의의 요청을 하게 만드는 공격

XSS = 클라이언트 측 브라우저에서 실행되는 스크립트를 삽입하는 공격

기존 비밀번호를 입력해야 하는 상황이라면 불가능하다.   
ex) yws/?oldpasswd=****    

그렇다면 XSS 취약점을 활용해야 한다.

GET, POST 간단 정리.   
GET  : URL   
POST : XSS 공격 연계   
```
<form method="POST">   
  <input>   
</form> 
```

## [3] Referer

Referer : 이 요청이 어디에서 한 건지 확인하는 부분

ex)   
/my-account → 내 계정에서 이 요청이 온 것이니까 ok 맞다.   
/board   → 게시판에서 왜 요청을 하지? CSRF 같네? 

유추 가능.
</br>

php referer check 검색해보자
</br>
</br>
</br>

비밀번호 변경 요청      
if referer 헤더가 있으면 → 검사 시작.   
else referer 헤더가 없으면 → 그냥 고!    
이런 경우가 있음.

이런 경우를 노려야 함.

\<meta name="referrer" content="no-referrer">

왜 referrer 이지?

## [4] CSRF Token

비밀번호를 바꾸려고 마이페이지를 입장하는 순간 마이페이지 안에서 csrf 토큰을 발행함.

csrf token(랜덤) 생성 → 세션에 저장 → 비교


### csrf_token을 받아오게 해서 넣어서 보내면 됨.

iframe에 의해서 csrf 토큰이 ifram 안으로 들어가게 됨.
자바스크립트에서 iframe 에 접근해서 파싱해서 가져온 다음에 보내면 됨.

iframe 2개 사용.
하나는 csrf 가져오기 위한 iframe   
또 하나는 form 가리기 위한 iframe