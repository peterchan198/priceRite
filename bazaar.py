import requests
import re
from bs4 import BeautifulSoup

r= requests.get('https://www.bazaarfurniture.co/products/%E9%AB%98%E6%9E%B6%E5%BA%8A%E9%85%8D%E9%9B%99%E9%9B%BB%E8%85%A6%E6%AA%AF%E7%B5%84%E5%90%88')
# r = r.text.encode(repr(r.encoding)).decode(requests.utils.get_encodings_from_content(r.text)[0])
# searched_word=re.compile(r'feed_variations\\":{\\"size\\":{\\"en\\":\\"\\",\\"zh-hant\\":\\"[0-9a-zA-Z\\"()\s}$]+')
content= re.findall(r'feed_variations\\":{\\"size\\":{\\"en\\":\\"\\",\\"zh-hant\\":\\"[0-9a-zA-Z\\"()\s}$]+' , r.text)
content= [x.replace('feed_variations\\":{\\"size\\":{\\"en\\":\\"\\",\\"zh-hant\\":\\"' ,'') for x in content]
content= [x.replace('\\' ,'') for x in content]

print(content)
# sidebar= BeautifulSoup(r.text, 'html.parser').find('ul', {'id':'sidebar'}).find_all('li')
# for x in sidebar:
#     href=x.find('a', href= True)['href']
#     pagelink=str('https://www.bazaarfurniture.co'+ href)
#
#     getLink = requests.get(str(pagelink))
#     bs = BeautifulSoup(getLink.text, 'html.parser')
#     items=bs.find('div', class_='class=boxify-container').find_all('li')
#     for x in items:
#         href_=x.find('a', href = True)['href']
#         link=str('https://www.bazaarfurniture.co'+ href)
#         getLink = requests.get(str(link))
#         bs = BeautifulSoup(getLink.text, 'html.parser')
#         databox=bs.find('div', class_='product-info row')
#         title=databox.find('h1').text
#         price=databox.find('div', class_= 'same-price').find('span', class_='price ng-binding').text
#         price = price.text[3:]
#         price = price.replace(',', '')
#         opt=bs.find()
#         des=bs.find('div', class_='global-secondary dark-secondary description-container').text
#         print(title)
#         print(price)
#         print(link)
