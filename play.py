import requests

rs = requests.session()
find_music_url = 'https://music.163.com/#/search/m/?s='+'安河桥'+'&type=1'
html = rs.get(find_music_url)
print(html.text)
