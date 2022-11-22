from crypt import methods
from dis import dis
from flask import Flask
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)


@app.route('/')
def helloworlds():

    htmlSourceCode = getHtmlSourceCode('watches')
    soup = BeautifulSoup(htmlSourceCode, 'html.parser')
    return htmlSourceCode

@app.route('/products', methods=['GET'])
#def hello():
def helloworld():

    htmlSourceCode = getHtmlSourceCode('watches')
    soup = BeautifulSoup(htmlSourceCode, 'html.parser')
    a_tags = soup.find_all('a', {'class':'s1Q9rs'})


    urls = list()

    for a in soup.find_all('a', {'class':'s1Q9rs'}):
        urls.append('https://www.flipkart.com/'+a['href'])

    for a in soup.find_all('a', {'class':'_1fQZEK'}):
        urls.append('https://www.flipkart.com/'+a['href'])

    for a in soup.find_all('a', {'class':'IRpwTa'}):
        urls.append('https://www.flipkart.com/'+a['href'])
    
    products = list()
    for url in urls:
        product = dict()

        page_soup = BeautifulSoup(requests.get(url).text, 'html.parser')

        name = page_soup.find('h1', {'class':'yhB1nd'})

        if name is None:
            product['name']= 'No name'
        else:
            product['name']= name.text
            
        price = page_soup.find('div', {'class':'_30jeq3 _16Jk6d'})
        
        if price is None:
            product['price']= 'No price'
        else:
            product['price']= price.text


        rating = page_soup.find('span', {'class':'_2_R_DZ _2IRzS8'})
        
        if rating is None:
            product['rating']= 'No rating'
        else:
            product['rating']= rating.text

        products.append(product)
    
    return {'products':products}

def getHtmlSourceCode(productName):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'T=TI166913628482800132137637577350621088825299692259538260309861944474; Network-Type=4g; pxcts=d67c2da6-6a86-11ed-b05f-516a427a4b45; _pxvid=d67c2052-6a86-11ed-b05f-516a427a4b45; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19319%7CMCMID%7C45980474997161701402441410798012315202%7CMCAAMLH-1669741087%7C3%7CMCAAMB-1669741087%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1669143488s%7CNONE%7CMCAID%7CNONE; _px3=c0600a11d8ab16aa10873efbeeb33b00b269850a46d0870704ad13e558df3e67:74n5BoMDCvUoZE5YE0/R7RgxZ1CnwLB8pKd7Oe3jvXj3L2Cwv0ih634MuV2afqayR/D62wW05D0oajyLHKp6RQ==:1000:2o2KKWpqm0uPB9u2R/WbTDsjH0tky7e/cNeo+7uS5pCWbEXnrFZzF7K4+6Dini/cZs3cVNq76u5XWJ7uhErnl4K0QJeQC3Egye9xh2T5UZ4h8rK4SFJ2hAdm4a3S4tmi+Aur7aG8wY9yANzORmsWMpI9Jy57nJJ7rXfaPCX9XgVxqNAKK7pX8pOkhZ8/hd+DuYCVixQXil23I4mjAzLP9w==; S=d1t15Pj8/Jz8/Kz8/PzQ/clN5Pzvsq6n2VKu5YETQ2YUZ7BTNaGp/8jSKY2O9WzarBxltdVAjcKp9YRa0qCtki43aDg==; qH=7d8949bcbf85067f; SN=VIB1F8BB64986A4A56B16D2D6F38FF29D2.TOKEF4D098582004744BEE9AAA309EFA00E.1669136364.LO',
        'Referer': 'https://www.google.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        }

    params = {
            'q': productName,
            'otracker': 'search',
            'otracker1': 'search',
            'marketplace': 'FLIPKART',
            'as-show': 'on',
            'as': 'off',
        }

    response = requests.get('https://www.flipkart.com/search', params=params, headers=headers)
    return response.text

if __name__=='__main__':
    app.run(debug=True)