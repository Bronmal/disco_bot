import requests
import os
from bs4 import BeautifulSoup

name_dir = r'\music_zay'
path = r'E:\программирование\disco_bot' + name_dir
URL_TRACK = 'https://zaycev.net/search.html?query_search='
MAIN_URL = 'https://zaycev.net'

class Zaycev():
    
    def download(self, song_name):
        # Достем сслыки на треки
        song_name = song_name.replace(' ', '+')
        response = requests.get(URL_TRACK + song_name)
        soup = BeautifulSoup(response.content, 'html.parser')
        urls_list = soup.find_all('a', class_='musicset-track__download-link track-geo__button')
        urls =[]
        for i in urls_list:
            urls.append(i.get('href'))
        urls = urls[0:5]

        # Сохраняем треки
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)

        path_song = path + f'\{song_name}'
        if not os.path.exists(path_song):
            os.makedirs(path_song)
            os.chdir(path_song)
            counter = 1
            for i in urls:
                r = requests.get(MAIN_URL + i)
                with open(song_name + str(counter) + '.mp3', 'wb') as f:
                    f.write(r.content)
                counter += 1