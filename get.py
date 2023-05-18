import requests

from datatime import get_today, get_tomorrow




async def get_picture():
    response = requests.get('https://mgok.mskobr.ru/roditelyam/vse-voprosi-o-pitanii')
    kolledj = response.text.find('Меню КОЛЛЕДЖ')
    menu = response.text.find(f'Меню на {await get_today()}', kolledj)
    d = ""
    for i in range(menu -110, menu, 1):
        d += (response.text[i])

    link = d.find('/attach')
    link2 = d.find('.jpg')

    g = ""
    for i in range(link, link2 + 4, 1):
        g += d[i]

    # print('https://mgok.mskobr.ru' + g)
    response = requests.get('https://mgok.mskobr.ru' + g)
    
    return response.content

async def tomorrow_picture():
    response = requests.get('https://mgok.mskobr.ru/roditelyam/vse-voprosi-o-pitanii')
    kolledj = response.text.find('Меню КОЛЛЕДЖ')
    menu = response.text.find(f'Меню на {await get_tomorrow()}', kolledj)
    if menu == -1:
        return "Меню ещё не выложили"
    else:
        d = ""
        for i in range(menu -110, menu, 1):
            d += (response.text[i])

        link = d.find('/attach')
        link2 = d.find('.jpg')

        g = ""
        for i in range(link, link2 + 4, 1):
            g += d[i]
        response = requests.get('https://mgok.mskobr.ru' + g)

        return response.content