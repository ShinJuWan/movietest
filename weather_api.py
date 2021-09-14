import requests
from bs4 import BeautifulSoup	

def getTemp():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=4&ie=utf8&query=%EB%82%A0%EC%94%A8"
    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('span',"todaytemp").get_text()
    return temp



