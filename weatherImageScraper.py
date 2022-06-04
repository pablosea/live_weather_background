import os
import sys
from lxml import html
from lxml import etree
import ctypes
import requests # request img from web

url = 'https://www.star.nesdis.noaa.gov/GOES/sector.php?sat=G16&sector=car'

session_requests = requests.session()
result = session_requests.get(url)
tree = html.fromstring(result.text)

url_list = tree.xpath('//*[@id="main"]/div/div[22]/div[2]/ul/li[7]/a/@href')

image_url = url_list[0]
file_destination = 'C:/Users/PJR/Pictures/weather/res.jpg'
res = requests.get(image_url)
if res.status_code == 200:  # http 200 means success
    with open(file_destination, 'wb') as file_handle:  # wb means Write Binary
        file_handle.write(res.content)
else:
    print('Download Failed')


ctypes.windll.user32.SystemParametersInfoW(20, 0, file_destination , 0)



