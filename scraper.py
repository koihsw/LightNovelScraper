import requests
from bs4 import BeautifulSoup


domain = "https://novelfull.net"
MAINURL = "https://novelfull.net/a-regressors-tale-of-cultivation.html"
url = MAINURL
urlResponse = requests.get(url).text

pageNum = 1
pageUrl = f"?page={pageNum}"

soup = BeautifulSoup(urlResponse, 'lxml')

# find all divs with the class "row"
div = soup.find_all('div', class_="row")

# print div with chapters list
chapterLinks = div[1].find_all('a')

# print(chapterLinks)
# print(len(chapterLinks))
# print(chapterLinks[len(chapterLinks) - 1])


try:
    print("Enter Chapter Number: ")
    enteredChapNum = int(input())
    if enteredChapNum == 0:
        print("0 is an invalid number")
    else:
        while True:
            if enteredChapNum > pageNum * 50:
                pageNum += 1
                pageUrl = f"?page={pageNum}"
                url = MAINURL + pageUrl

            elif enteredChapNum < pageNum * 50:
                print("break")

                urlResponse = requests.get(url).text
                soup = BeautifulSoup(urlResponse, 'lxml')
                # find all divs with the class "row"
                div = soup.find_all('div', class_="row")

                # find all 'links' in the div
                chapterLinks = div[1].find_all('a')
                print(chapterLinks)
                break
 
        print((enteredChapNum - 1) - ((pageNum - 1) * 50))
        chapterObj = chapterLinks[(enteredChapNum - 1) - ((pageNum - 1) * 50)]
        print(chapterObj['title'])
        url = domain + chapterObj['href']
        print(url)
        
        urlResponse = requests.get(url).text
        soup = BeautifulSoup(urlResponse, 'lxml')
        chpContent = soup.find("div", id="chapter-content")

        # Get all paragraphs in chpContent
        allP = chpContent.find_all("p")

        # append to newList to print the output
        newLis = []
        with open("chapter.txt", "w", encoding="utf-8") as chapter:
            chapter.write(f"{chapterObj['title']}\n")
            for p in allP:
                if p.text != "":
                    print(p.text)
                    newLis.append(p.text)
                    chapter.write(f"{p.text}\n")
                elif p.text == "":
                    print("removed blank")
                    allP.remove(p)
except ValueError:
    print("String not allowed")
