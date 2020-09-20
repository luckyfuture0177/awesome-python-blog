from urllib import request, parse

with request.urlopen('https://blog.llloverr.com/') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        # 打印请求头中的信息
        print('%s: %s' % (k, v))

# Get请求 使用Request对象
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# 模拟手机请求
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # print('Data:', f.read().decode('utf-8'))


# Post 把参数data以bytes形式传入
login_data = parse.urlencode([
    ('username', ),
    ('password', ),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    pass






