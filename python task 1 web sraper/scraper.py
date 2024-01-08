import requests
from bs4 import BeautifulSoup

url = 'https://blog.hubspot.com/blog/tabid/6307/bid/34143/12-inspiring-examples-of-beautiful-blog-homepage-designs.aspx'


# get the html contents 
req = requests.get(url)
html = req.content
print(html)


# parse the html content
soup = BeautifulSoup(html,'html.parser')
print(soup)
print('soup is printed')


# print paragraphs elements
paragraph = soup.find_all('p')
print( paragraph)
for paragraphs in paragraph:
    if(paragraphs.get('text') != ''):
        print(paragraphs)

#print anchors element
anchors = soup.find_all('a')
print(anchors)

for link in anchors:
    if(link.get('href') != '#'):
        print(link)

# print image element
image = soup.find_all('img')
print(image)

for images in image:
    if(images.get('src') != '#'):
        print(images)
