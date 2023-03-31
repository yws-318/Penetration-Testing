# VMware의 MySQL을 윈도우의 DBeaver로 외부 접속 연결 방법
MySQL version : 8.0.32<br />
<br />
mysql 유저 권한 설정이 끝났다면 <br />
<br />
sudo ufw enable<br />
<br />
sudo ufw allow 3306<br />
<br />
sudo ufw status<br />
<br />
cd /etc/mysql/mysql.conf.d/<br />
<br />
ls<br />
<br />
sudo nano mysqld.cnf<br />
<br />
들어가서 <br />
<br />
bind-address = 127.0.0.1<br />
mysqlx-bind-address = 127.0.0.1<br />
<br />
위 두 코드를 주석처리 (#)<br />
<br />
Ctrl + s : 저장하기<br />
Ctrl + x : 나가기<br />
<br />
sudo systemctl restart mysql<br />
<br />
netstat -nap | grep LISTEN<br />
LISTEN 상태인 포트만 출력<br />
<br />
ifconfig<br />
<br />
inet ***.***.***.*** <br />
<br />
ip 확인 후 <br />
<br />
(DBeaver)<br />
새로운 db연결<br />
Server Host : ***.***.***.***<br />
Port        : 3306<br />
Database    : energy<br />
Username    : yws<br />
Password    : ********<br />
<br />
Test Connection 연결 상태 확인<br />
<br />
(VMware) 
Edit - Virtual Network Editer<br />
Change Settings<br />
<br />
ifconfig inet과 비슷한 ip확인 후 Host Connetion이 Connected가 아니라면<br />
<br />
VMnet* 클릭 - Connect a host virtual adapter to this network (check)<br />
Apply - OK<br />
<br />
(DBeaver) <br />
Test Connection<br />
<br />
완료.<br />
<br />