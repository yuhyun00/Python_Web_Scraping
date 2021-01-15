import requests
from bs4 import BeautifulSoup

codes = ['005930', '096530'] # 종목코드 리스트 ['삼성전자', '씨젠']
names = [] # 이름정보가 담길 리스트
prices = [] # 가격정보가 담길 리스트

for code in codes:
    url = 'https://finance.naver.com/item/main.nhn?code=' + code

    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    wrap_company = soup.select_one('#middle > div.h_company > div.wrap_company')
    name = wrap_company.select_one('h2')
    names.append(name.get_text())

    today = soup.select_one('#chart_area > div.rate_info > div')
    price = today.select_one('.blind')
    prices.append(price.get_text())

print(names)
print(prices)