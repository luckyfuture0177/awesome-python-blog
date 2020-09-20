from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)
def event(url):
    req = request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')
    with request.urlopen(req) as rep:
        data = rep.read().decode('utf-8')

    match_title = re.findall('<h3.*<a.*>(.*?)</a>', data)
    match_time = re.findall('<time.*00">(.*)</span>', data)
    match_time_true = []
    for time in match_time:
        match_time_true.append(time.replace('<span class="say-no-more">', ' '))
    match_place = re.findall('event-location">(.*?)</span>', data)
    '''
    print(match_time_true)
    print(match_title)
    print(match_place)
    print(len(match_time_true), len(match_title), len(match_place))
    '''
    for i in range(0,len(match_place)):
        print('名称：',match_title[i])
        print('时间：', match_time_true[i])
        print('地点：', match_place[i])
        print('\n')

if __name__ == '__main__':
    target = 'https://www.python.org/events/python-events/?page='
    for i in range(1, 5):
        print('Page', i)
        url = target+str(i)
        event(url)













