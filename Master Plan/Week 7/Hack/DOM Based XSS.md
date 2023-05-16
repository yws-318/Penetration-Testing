# DOM Based XSS

DOM 기반 XSS 공격은 보안에 취약한 JavaScript 코드로 DOM 객체를 제어하는 과정에서 발생.

DOM 기반 XSS 공격 시나리오.
```
1. 보안이 취약한 웹 페이지에서 악성 스크립트가 실행되도록 URL 주소를 만들어 일반 사용자에게 전달.
2. 일반 사용자는 메일 등을 통해 전달받은 URL 링크를 클릭한다. 서버로부터 HTML 문서를 전달받는다.
3. 사용자의 브라우저가 응답 받은 HTML 문서를 읽으면서 필요한 스크립트를 실행하는 중에 악성 스크립트가 동작한다.
4. 악성 스크립트를 통해 사용자가 정보를 악의적으로 전달된다.
```

이 공격은 Reflected XSS와는 다르게 서버로 요청을 보내지 않아도 스크립트를 심을 수 있다.

URL의 javascript 코드를 만나 해당 스크립트가 실행된다.

```
원래

<script>
    var img = new Image();
</script>
```
```
DOM 버전

<script type="text/javascript">
    function serach()
    {
        var myurl = document.URL;
        if(myurl.indexOf("?search=")>0)
        {
            document.getElementById('srch').innerHTML = "You've searched for "+unescpae(myurl.substr(myurl.indexOf
            ("?search=")+8));
        }
    }
</script>
```

indexOf에서 공격

Reflect XSS와 다르게 찾기 힘들다.   

DOM Based XSS를 찾는 방법   
1.화면을 잘 봐라   
2. 볼만한 아이들   
1. javascript
2. new Image();      
3. document.innerHTML