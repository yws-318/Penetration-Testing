# OTP 우회

우선 OTP 우회 링크를 타고 들어가면 로그인 화면이 아닌    
"핵미사일 시스템" 이라는 화면이 우선적으로 나온다.

![1](https://user-images.githubusercontent.com/106296883/231666116-109191b3-fcc5-46dd-8334-a4bde4a18d83.PNG)
</br>
</br>
</br>

Fire 버튼을 눌르면
![2](https://user-images.githubusercontent.com/106296883/231666108-7fbb7707-b37a-4562-9c8d-6d5749aed8b9.PNG)

이런 식으로 관리자만 이용 가능하다는 문구가 나온다.
</br>
</br>
</br>

다시 확인을 누르면 
![3](https://user-images.githubusercontent.com/106296883/231666114-0b8fe615-c271-4021-a70c-fd1e37944578.PNG)

POST 형식으로 비밀번호를 입력하라는 입력창이 나온다.

우리가 알고 있는 취약점 분석 방법은 많지 않다.

Cookie를 이용해서 admin 권한을 탈취하는 게 전부일 정도.

하지만 Cookie에는 아무런 정보를 얻을 수 없다.

힌트는 url에 있다.
</br>
</br>
</br>


## URL
---

Fire 버튼을 눌렀을 때 이동했던 url을 자세히 살펴보자.

```
step1.php
```

확인을 눌렀을 때의 url을 확인해보면

```
step2.php
```

그렇다면 세 번째 단계의 url은?  

step3.php 라고 유추해볼 수 있다.

```
step3.php
```

step3.php 를 입력했더니 
![4](https://user-images.githubusercontent.com/106296883/231723587-e03f7892-a450-41bc-b573-d4ac0f8f6031.PNG)

해당 화면이 나왔다.

Fire 버튼을 눌러보니

![5](https://user-images.githubusercontent.com/106296883/231723820-a24b2ae3-d24a-4cd1-bcde-d5d203ef291b.PNG)

flag가 나왔다.

이런식으로 유추가 가능한 url을 설정해두면 인증에 회피할 수 있다는 것을 명심하자.   
웹개발할 때 중요하게 봐야하는 부분이다.