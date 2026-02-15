import requests
from bs4 import BeautifulSoup


domain = "https://novelfull.net"
MAINURL = "https://novelfull.net/a-regressors-tale-of-cultivation.html"
url = MAINURL
urlResponse = requests.get(url).text

soup = BeautifulSoup(urlResponse, 'lxml')

lChapters = soup.find("ul", class_="l-chapters")

print(lChapters)

chapterList = soup.find_all("ul", class_="list-chapter")

links = []

for element in range(len(chapterList)):
    
    temp = chapterList[element].find_all("a")
    for chapterNum in range(len(temp)):
        print(temp[chapterNum]['title'])

    links.append(chapterList[element].find_all("a"))
    # print(chapterList[element].find_all("a")[0]['title'])

    # print(links[0]['title'])

# there are two arrays inside "links"
print(links[0][0]['title'])
