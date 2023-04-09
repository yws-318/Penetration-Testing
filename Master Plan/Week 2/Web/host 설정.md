# 호스트 설정

hosts 파일을 설정해서 가상의 도메인을 브라우저에 입력했을 때 localhost로 연결되도록 설정한다.

해당 경로로 hosts 파일을 연다.
```
sudo nano /etc/hosts
```
```
127.0.0.1       yang.com
```

url로 잘 접속이 되는지 확인.
```
http://www.yang.com
```
