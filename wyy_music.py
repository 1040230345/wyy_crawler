from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

driver = None


# 启动浏览器
def open_chrome():
    # 调试器配置
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面.
    # chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" #手动指定使用的浏览器位置
    # 申明是谷歌浏览器
    global driver
    driver = webdriver.Chrome(chrome_options=chrome_options)


# 查找音乐
def find_music(your_music):
    # 访问地址
    find_music_url = 'https://music.163.com/#/search/m/?s='+your_music+'&type=1'
    driver.get(find_music_url)
    # driver.implicitly_wait(5)
    driver.switch_to.frame('g_iframe')  # 进入iframe
    find_music_html = driver.execute_script("return document.documentElement.outerHTML")
    # print(html)
    # 规范化输出
    soup = BeautifulSoup(find_music_html, 'lxml')
    # 查找的类名
    attrs = {
        'class': 'item',
        'class': 'f-cb',
        'class': 'h-flag'
    }
    # 查找类名为attrs的内容
    find_music1 = soup.findAll(name="div", attrs=attrs)
    # 查找后的音乐列表
    find_ok_music = []
    for my_music in find_music1:
        # 取值
        a = my_music.find_all('a')[1]
        b = my_music.find_all('b')
        c = BeautifulSoup(str(my_music), 'lxml').findAll(name="div", attrs={'class': 'text'})[1]
        c = BeautifulSoup(str(c), 'lxml').get_text()
        span = my_music.find_all('div')[11]
        music_time = BeautifulSoup(str(span), 'lxml').get_text()
        # 查找内容存放
        find_my_music = {
            'a': a['href'],  # 歌曲链接
            'b': b[0]['title'],  # 歌曲名称
            'c': c,  # 演唱者
            'time': music_time  # 歌曲时间
        }
        find_ok_music.append(find_my_music)
    # for aaa in find_ok_music:
    #     print(aaa)
    return find_ok_music


# 关闭浏览器
def close_chrome():
    driver.close()  # 关闭浏览器，回收资源


