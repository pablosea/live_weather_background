import os
import sys
from lxml import html
from lxml import etree
import ctypes
import requests # request img from web

#NOAA URL
url = 'https://www.star.nesdis.noaa.gov/GOES/sector.php?sat=G16&sector=car'

#Open webpage
session_requests = requests.session()
result = session_requests.get(url)
tree = html.fromstring(result.text)

#xpath to image URL
url_list = tree.xpath('//*[@id="main"]/div/div[5]/div[2]/ul/li[7]/a/@href')

#xpath returns link as a list, this just pulls link text out of the list
image_url = url_list[0]

file_destination = 'C:/Users/PJR/Pictures/weather/res.jpg'

#grab image
res = requests.get(image_url)

#check if image was installed
if res.status_code == 200:  # http 200 means great success
    with open(file_destination, 'wb') as file_handle:  # wb means Write Binary
        file_handle.write(res.content)
else:
    print('Download Failed')

#update desktop background
ctypes.windll.user32.SystemParametersInfoW(20, 0, file_destination , 0)



