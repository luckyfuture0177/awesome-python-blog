from urllib import request
import json
# 获取json数据并解析为python对象
def fetch_data(url):
    req = request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')
    with request.urlopen(req) as rep:
        # print('Data:', rep.read().decode('utf-8'))
        json_str = rep.read().decode('utf-8')
        print(json_str)
        user_dic = json.loads(json_str)
        return user_dic
obj = fetch_data('http://www.httpbin.org/get')
print(obj['headers']['Host'])
