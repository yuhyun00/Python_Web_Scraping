from urllib.request import urlopen

html = urlopen('https://finance.naver.com/')
print(html.read())
