# SSRF 

SSRF (Server Side Request Forgery)

CSRF = Client   
SSRF = Server

SSRF는 어디에서 일어나느냐?   
1.서버가 외부 자원(리소스)를 이용하는 곳에서 발생.   
2.파라미터로 URL을 받는 경우에서 일어남.

ex)   
날씨 정보를 출력해주는 기능이 있을 경우.   
날씨 정보를 가져오는 API를 파라미터로 넣어서 URL을 입력하는 경우   
view.php/weatherAPI=htts://기상청.com/~~~   

만약 날씨 정보를 주는 API 주소를 지우고,   
내가 원하는 URL을 넣는다면   
이 요청을 내가 원하는 곳으로 날리게 만들 수 있다.

## 대응방안

파라미터로 API 주소를 그대로 받으면 안됨.
