import os

import requests

from bs4 import BeautifulSoup
from tqdm import *
from time import sleep


def downloading(tag):
    url = f"https://danbooru.donmai.us/posts?d=1&tags={tag}&api_key=hoJuQCDHNRt8VW4ETemKPaNp&login=Klaksik"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    max_numbers = soup.find_all("a", class_="paginator-page desktop-only")
    max_number = (int(max_numbers[4].get_text()))

    print(f'страниц {max_number}')

    list_url_art = []
    links = []
    i = 0
    for num in trange(max_number):
        i += 1
        print(f'\nстраница номер: {i}, осталось {max_number - i} страниц')

        url = f"https://danbooru.donmai.us/posts?api_key=hoJuQCDHNRt8VW4ETemKPaNp&d=1&login=Klaksik&page={num}&tags=order%3Arank"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")
        pages = soup.find_all("a", class_="post-preview-link")

        for img in pages:
            link = img.get("href")

            links.append(f'https://danbooru.donmai.us{link}')
        for art in links:
            #sleep(150)
            response = requests.get(art)
            soup = BeautifulSoup(response.text, "html.parser")
            imgs = soup.find_all("img", id="image")
            for img in imgs:
                link = img.get("src")
                list_url_art.append(link)

        folder_name = 'ph'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        for art in list_url_art:
            #sleep(150)
            response = requests.get(art)
            file_name = os.path.join(folder_name, os.path.basename(art))
            if response.status_code == 200:
                with open(file_name, 'wb') as imgfile:
                    imgfile.write(response.content)
                    #sleep(150)


