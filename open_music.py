import requests
from music import music_data as md
from bs4 import BeautifulSoup
import urllib


def jiemi():
    # 构造请求字典
    query = {
        'csrf_token': "",
        'encodeType': "aac",
        'ids': "[566521546]",
        'level': "standard"
    }
    # 解密
    do = md.Encrypyed()
    # 请求参数
    data = do.d(query)
    print(data)
    # 开始请求
    r = requests.session()
    # 请求头
    headers = {
        'origin': 'https: // music.163.com',
        'referer': 'https: // music.163.com /',
        'user - agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    # 请求url
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
    html = r.post(url, data=data, headers=headers)
    song_url = html.json()['data'][0]['url']
    print(song_url)
    # print(html.json())


# 下载音乐
def login_music(music_id):
    # 下载
    res = requests.get('http://music.163.com/song/media/outer/url?id='+music_id+'.mp3')
    try:
        res.raise_for_status()
    except Exception as exc:
        print('there was a problem: %s' % (exc))
    # 方法1
    # playFile = open('my_music/123'+'.mp3', 'wb')
    #
    # # iter_content方法，循环的每次迭代中
    # for chunk in res.iter_content(1000000):
    #     # 把每次迭代内容写入文件
    #     playFile.write(chunk)
    # playFile.close()
    # 方法2
    with open('my_music/'+music_id+'.mp3', 'wb') as f:
        f.write(res.content)
        f.close()


