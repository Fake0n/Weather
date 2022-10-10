import requests
from pprint import pprint
import datetime


APPID = '7e5e7bb1bbb117bdea9074844d36fc36'
url = (f"https://api.openweathermap.org/data/2.5/forecast?lat=43.43&lon=39.91&lang=ru&appid={APPID}&units=metric")

weather = requests.get(url).json()
today = datetime.date.today()
tomorow = today + datetime.timedelta(days=1)
tomorow = str(tomorow)

city = weather['city']['name']
print(f'Город : {city}')


for list in weather['list']:
    check = list['dt_txt'][0:10].strip()
    if tomorow == check:
        date_time = list['dt_txt'][10:].strip()
        temp = list['main']['temp']
        feels_like = list['main']['feels_like']
        temp_max = list['main']['temp_max']
        temp_min = list['main']['temp_min']
        print(f'Время : {date_time}', f'Температура : {temp}', f'Ощущается как : {feels_like}', f'Максимальная температура : {temp_max}', f'Минимальная температура : {temp_min}',sep=('\n'))
        for weath in list['weather']:
            weth = weath['description']
            print(f'Погода : {weth.capitalize()}')
        wind = list['wind']['speed']
        print(f'Скорость ветра : {wind}')
        print('#####################################')
