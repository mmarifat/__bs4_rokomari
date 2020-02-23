# Author Minhaz Ahamed<mma.rifat66@gmail.com>
# Email: mma.rifat66@gmail.com
# Web: https://mma.champteks.us
# Do not edit file without permission of author
# All right reserved by Minhaz Ahamed<mma.rifat66@gmail.com>
# Created on: 23/02/2020 8:26 PM

import requests
from bs4 import BeautifulSoup
import csv

url = 'http://www.rokomari.com/book/category/2407/book-fair-2020-?sort=&page=1'

res = requests.get(url).text
try:
    bookContent = BeautifulSoup(res, 'html.parser')
    pagination = bookContent.find("div", class_='pagination')
    totalPage = pagination.find_all('a')
    page = int(totalPage[len(totalPage) - 2].text)
    # print(page)

    for x in range(page + 1):
        # manipulate link
        sourceCode = requests.get(url + str(x + 1)).text

        # BeautifulSoup object
        soup = BeautifulSoup(sourceCode, 'html.parser')

        # Collect everything from <div> tags with class <book-list-wrapper>
        for eachBook in soup.find_all('div', {'class': 'book-list-wrapper'}):
            content = []
            bookTitle = eachBook.find('p', {'class': 'book-title'}).text
            bookAuthor = eachBook.find('p', {'class': 'book-author'}).text
            bookStatus = eachBook.find('p', {'class': 'book-status'}).text
            try:
                bookOrgPrice = eachBook.find('p', {'class': 'book-price'}).strike.text
            except:
                bookOrgPrice = ''
            bookPrice = eachBook.find('p', {'class': 'book-price'}).span.text

            content.append([bookTitle, bookAuthor, bookStatus, bookOrgPrice, bookPrice])
            print(content)

            with open("rokomariBookFair2020.csv", 'a', newline='', encoding='utf-8') as csvfile:
                csvfile.write('\ufeff')
                writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
                writer.writerows(content)

except Exception as e:
    print(e)
