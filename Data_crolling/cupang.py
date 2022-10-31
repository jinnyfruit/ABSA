import requests
from bs4 import BeautifulSoup
import re, openpyxl

print("1")
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
res = requests.get("https://www.coupang.com/np/search?component=&q=%EC%95%84%EC%9D%B4%ED%8F%B0&channel=user", headers = headers)

print("2")
soup = BeautifulSoup(res.content, 'html.parser')

print("3")
product_name = soup.select('div > div.name')
product_price = soup.select('div.price-wrap > div.price > em > strong')
product_review = soup.select('div.other-info > div > span.rating-total-count')
product_link = soup.select('a.search-product-link')

print("4")
excel = openpyxl.Workbook()
sheet = excel.active

print("5")
sheet.title = "쿠팡 상품 정보 크롤링하기"
sheet.append(['상품명', '가격', '리뷰 수', '상품 링크'])

print("6")
sheet.column_dimensions['A'].width = 60
sheet.column_dimensions['B'].width = 12
sheet.column_dimensions['C'].width = 10
sheet.column_dimensions['D'].width = 10

A1_cell = sheet['A1']
A1_cell.alignment = openpyxl.styles.Alignment(horizontal='center')
A1_cell.font = openpyxl.styles.Font(color='0055FF')

B1_cell = sheet['B1']
B1_cell.alignment = openpyxl.styles.Alignment(horizontal='center')
B1_cell.font = openpyxl.styles.Font(color='0055FF')

C1_cell = sheet['C1']
C1_cell.alignment = openpyxl.styles.Alignment(horizontal='center')
C1_cell.font = openpyxl.styles.Font(color='0055FF')

D1_cell = sheet['D1']
D1_cell.alignment = openpyxl.styles.Alignment(horizontal='center')
D1_cell.font = openpyxl.styles.Font(color='0055FF')

idx = 2
for name, price, review, link in zip(product_name, product_price, product_review, product_link):
    p_name = name.text
    p_price = price.text
    p_review_cnt = re.sub("[()]","", review.text)
    p_link = "https://coupang.com" + link['href']
    
    sheet.append([p_name, p_price, p_review_cnt, '이동하기'])
    sheet.cell(row=idx, column=4).hyperlink = p_link
    
    idx += 1

excel.save('coupang_item_list.xlsx')