from bs4 import BeautifulSoup
import urllib.request

request = urllib.request.urlopen('https://24.kg/kyrgyzcha/')
html = request.read()
mSoup = BeautifulSoup(html,'html.parser')
news = mSoup.find_all('div', class_='one')
# print(news)
results = []
for item in news:
    date = item.find('div', class_='time').get_text(strip=True)
    title = item.find('div',class_='title').get_text(strip=True).replace("&nbsp;", "")
    href = item.a.get('href')
    results.append({
        'date': date,
        'title': title,
        'href': href,
    })
file = open('news.txt','w',encoding='utf-8')
count = 1
for newsItem in results:
    file.write(f'Жанылыктар № {count}\n'
               f'Убактысы: {newsItem["date"]}\n'
               f'Жанылыктардын темасы: {newsItem["title"]}\n'
               f'Жанылыктын шилтемеси: {newsItem["href"]}\n---------------------\n\n')
    count +=1
print(results)