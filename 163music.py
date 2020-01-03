# _*_ encoding:utf-8 _*_
__author__ = 'hsurich'
__date__ = '2020/1/3 19:29'
import requests
from bs4 import BeautifulSoup
import os

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
    # 'referer': 'http://93.174.95.27',
    # referer告诉服务器该网页是从哪个页面链接过来的
}
# link = "https://music.163.com/discover/toplist?id=3778678"
link = 'https://music.163.com/playlist?id=29395816'
r = requests.get(link, headers=header)
html = r.content
soup = BeautifulSoup(html, "html.parser")     # 通过Beautifulsoup解析网页
# print(soup)
songs = soup.find("ul", class_="f-hide").select("a", limit=100)
# print(songs)
#
i = 1

# 如果没有，则创建music文件夹
folder = 'music'
if not os.path.exists(folder):
    os.makedirs(folder)

for s in songs:
    song_id = s['href'][9:]
    song_name = s.text + '.mp3'
    path = os.path.join(folder, song_name)
    print(path)
    try:
        download_link = "http://music.163.com/song/media/outer/url?id="+song_id + '.mp3'
        print('第' + str(i) + '首歌曲' + download_link)
        print('正在下载中...')

        response = requests.get(download_link, headers=header).content
        f = open(path, 'wb')
        f.write(response)
        f.close()
        print("下载完成.\r\n")
    except Exception as e:
        print("下载失败.."+str(e))
    i += 1

