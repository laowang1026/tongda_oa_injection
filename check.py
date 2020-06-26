import urllib.request
import time
import requests
 
opener = urllib.request.build_opener()
file = open('url.txt')
lines = file.readlines()
print('开始检查：')
for line in lines:
    i=str(line.replace("\n",""))
    url = "http://"+i+"/general/management_center/portal/oa_engine/engine_manage_bulletin_number/query.php"
    tempUrl = url
    try :
        opener.open(tempUrl)
        if (len(requests.get(tempUrl).text) == 0):
            print(i+"存在漏洞")
    except urllib.error.HTTPError:
        time.sleep(1)
    except urllib.error.URLError:
        time.sleep(1)
    time.sleep(0.1)
