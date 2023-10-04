import requests
import asyncio
from urllib.parse import urljoin
from datatime import get_today, get_tomorrow, get_dweek
from bs4 import BeautifulSoup


async def get_picture():
    response = requests.get('https://mgok.mskobr.ru/roditelyam/vse-voprosi-o-pitanii') # получает код страницы
    html = response.text # сохраняет код страницы в переменную html
    soup = BeautifulSoup(html, 'html.parser') # Анализирует код страницы
    today = await get_today()
    menu = soup.find_all(lambda tag: tag.name == 'li' and f'Меню Вишнёвая {today}' in tag.text) # по идее ищет в коде страницы указанный текст
    g = 'https://mgok.mskobr.ru'
    
    links = [link.get('href') for item in menu if (link := item.find('a'))]
    if link:
        for link in links:
            full_url = urljoin(g,link)
            content = requests.get(full_url)    
            image_data = content.content
            return image_data
# async def get_picture():
#     response = requests.get('https://mgok.mskobr.ru/roditelyam/vse-voprosi-o-pitanii')
#     kolledj = response.text.find('Меню КОЛЛЕДЖ')
#     menu = response.text.find(f'Меню на {await get_today()}', kolledj)
#     d = ""
#     for i in range(menu -110, menu, 1):
#         d += (response.text[i])

#     link = d.find('/attach')
#     link2 = d.find('.jpg')

#     g = ""
#     for i in range(link, link2 + 4, 1):
#         g += d[i]

#     # print('https://mgok.mskobr.ru' + g)
#     response = requests.get('https://mgok.mskobr.ru' + g)
    
#     return response.content

async def tomorrow_picture():
    response = requests.get('https://mgok.mskobr.ru/roditelyam/vse-voprosi-o-pitanii') # получает код страницы
    html = response.text # сохраняет код страницы в переменную html
    soup = BeautifulSoup(html, 'html.parser') # Анализирует код страницы
    tomorrow = await get_tomorrow()
    menu = soup.find_all(lambda tag: tag.name == 'li' and f'Меню Вишнёвая {tomorrow}' in tag.text) # по идее ищет в коде страницы указанный текст
    g = 'https://mgok.mskobr.ru'

    links = [link.get('href') for item in menu if (link := item.find('a'))]
    for link in links:
        full_url = urljoin(g,link)
        content = requests.get(full_url)
        image_data = content.content
        return image_data

# async def pari_picture():
#     content = requests.get("https://i.imgur.com/YGT9HLd.png")
#     return content.content

# async def ponedelnik_picture():
#     image = requests.get('https://i.imgur.com/jWFVHGF.png')
#     return image.content

# async def vtornik_picture():
#     image = requests.get('https://i.imgur.com/JpSD7cK.png')
#     return image.content

# async def sreda_picture():
#     image = requests.get('https://i.imgur.com/oXnmliZ.png')
#     return image.content

# async def Thursday_picture():
#     image = requests.get('https://i.imgur.com/6kdhwXI.png')
#     return image.content

# async def friday_picture():
#     image = requests.get('https://i.imgur.com/oeH9Zw5.png')
#     return image.content

async def Weekend():
    image = requests.get('https://i.imgur.com/Ws49DUI.jpeg')
    return image.content

dni = {
    0: "https://i.imgur.com/jWFVHGF.png",
    1: "https://i.imgur.com/JpSD7cK.png",
    2: "https://i.imgur.com/oXnmliZ.png",
    3: "https://i.imgur.com/6kdhwXI.png",
    4: "https://i.imgur.com/oeH9Zw5.png"
}


async def get_picture_dweek():
    dweek = await get_dweek()
    a = len(dni)
    weekend = await Weekend()
    if dweek >= a:
        return weekend
    else:
        src = dni.get(dweek)
        image = requests.get(src)
        return image.content
















async def main():
    content = await get_picture()
    print(content)


if __name__ == "__main__":
    asyncio.run(main())



# async def tomorrow_picture():
#     response = requests.get('https://mgok.mskobr.ru/roditelyam/vse-voprosi-o-pitanii')
#     kolledj = response.text.find('Меню КОЛЛЕДЖ')
#     menu = response.text.find(f'Меню на {await get_tomorrow()}', kolledj)
#     if menu == -1:
#         return "Меню ещё не выложили"
#     else:
#         d = ""
#         for i in range(menu -110, menu, 1):
#             d += (response.text[i])

#         link = d.find('/attach')
#         link2 = d.find('.jpg')

#         g = ""
#         for i in range(link, link2 + 4, 1):
#             g += d[i]
#         response = requests.get('https://mgok.mskobr.ru' + g)

#         return response.content