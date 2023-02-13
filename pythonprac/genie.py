import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
'''#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis  #제목검사시 복사후 붙여놓은거
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number					     #순위검사시 복사후 붙여놓은거'''
for tr in trs:
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()								  #strip() : 문자열 및 공백 제거
    rank = tr.select_one('td.number').text[0:2].strip()												  
    artist = tr.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, artist)