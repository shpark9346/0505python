from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "https://music.bugs.co.kr/chart"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
rank = 1

results = soup.findAll('p', "title")
openfile = open("practice.txt", "a", encoding="UTF-8")

openfile.write(str(datetime.now()) + "의 벅스 실시간 차트 순위입니다.\n")

for result in results:
    openfile.write(str(rank) + "위:" + str(result.get_text()))
    rank += 1