import requests
from bs4 import BeautifulSoup
import pandas as pd

# url = "https://www.google.com/search?q=%E3%83%97%E3%83%AD%E9%87%8E%E7%90%83+%E8%A9%A6%E5%90%88%E7%B5%90%E6%9E%9C&rlz=1C1TENE_jaJP1058JP1058&oq=%E3%83%97%E3%83%AD%E9%87%8E%E7%90%83%E3%80%80%E8%A9%A6%E5%90%88%E7%B5%90%E6%9E%9C&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIICAUQABgHGB4yBwgGEAAYgAQyCggHEAAYBxgPGB4yBggIEAAYHjIGCAkQABge0gEINTc3MWowajSoAgiwAgE&sourceid=chrome&ie=UTF-8#sie=lg;/g/11sv_s3l9j;4;/m/012xwy;mt;fp;1;;;"
# url = "http://bee-planetz.com"
url = "https://www.yomiuri.co.jp/"
res = requests.get(url)

if res.status_code == 200:
    soup = BeautifulSoup(res.content, "html.parser")
    
    # elems = soup.select("body > div.uni-home > div > main > div.home-l-main__primary > section.home-headline > div.home-headline__contents > div > div.hero > div.item > h3 > a")
    parent_el = soup.find_all(class_="title")
    print(parent_el)

    # matches = []

    # for match in soup.find_all("div", class_="v-list-item__title mb-2 font-weight-bold"):
    #     print(match)