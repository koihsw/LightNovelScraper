import requests
from bs4 import BeautifulSoup


domain = "https://novelfull.net"

# target url
MAINURL = "https://novelfull.net/a-regressors-tale-of-cultivation.html"
url = MAINURL

# chapter count 
chCount = 0

# page number
pageNum = 0
pageUrl = f"?page={pageNum}"

urlResponse = requests.get(url).text
soup = BeautifulSoup(urlResponse, 'lxml')

# latest chapters list, first item in the list is the latest chapter
lChaptersList = soup.find("ul", class_="l-chapters")
lastestCh = lChaptersList.find("a")

latestFound = False

print(lastestCh['title'])

links = []
while latestFound == False:

    pageNum += 1
    pageUrl = f"?page={pageNum}"
    url = MAINURL + pageUrl

    urlResponse = requests.get(url).text
    soup = BeautifulSoup(urlResponse, 'lxml')

    chapterList = soup.find_all("ul", class_="list-chapter")
    
    for element in range(len(chapterList)):
        
        temp = chapterList[element].find_all("a")
        for chapterNum in range(len(temp)):
            print(temp[chapterNum]['title'])
            chCount += 1
            if temp[chapterNum]['title'] == lastestCh['title']:
                print("found")
                latestFound = True
            # links.append(temp[chapterNum])

    print(chCount)
    print(pageNum)
    print(url)
