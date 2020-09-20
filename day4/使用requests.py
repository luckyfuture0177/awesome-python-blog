import requests
import re


def event(url):
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
    data = requests.get(url, headers=headers)
    data = data.text

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
