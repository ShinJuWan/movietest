from weather_model import WeatherModel
import requests
from bs4 import BeautifulSoup	

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=4&ie=utf8&query=%EB%82%A0%EC%94%A8"

response = requests.get(url)

if (response.status_code == 200):
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    temps = soup.find(["span"],["todaytemp"])
    print(temps)


