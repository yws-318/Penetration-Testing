# VMware의 MySQL을 윈도우의 DBeaver로 외부 접속 연결 방법
MySQL version : 8.0.32

mysql 유저 권한 설정이 끝났다면 

sudo ufw enable

sudo ufw allow 3306

sudo ufw status

cd /etc/mysql/mysql.conf.d/

ls

sudo nano mysqld.cnf

들어가서 

bind-address = 127.0.0.1
mysqlx-bind-address = 127.0.0.1

위 두 코드를 주석처리 (#)

Ctrl + s : 저장하기
Ctrl + x : 나가기

sudo systemctl restart mysql

netstat -nap | grep LISTEN
~LISTEN 상태인 포트만 출력~

ifconfig

inet ***.***.***.***

ip 확인 후 

(DBeaver)
새로운 db연결
Server Host : ***.***.***.***
Port        : 3306
Database    : energy
Username    : yws
Password    : ********

Test Connection 연결 상태 확인

(VMware) 
Edit - Virtual Network Editer
Change Settings

ifconfig inet과 비슷한 ip확인 후 Host Connetion이 Connected가 아니라면

VMnet* 클릭 - Connect a host virtual adapter to this network (check)
Apply - OK

(DBeaver) 
Test Connection

완료.