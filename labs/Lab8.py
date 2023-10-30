import requests
from bs4 import BeautifulSoup


url = 'https://www.nike.com/t/pegasus-40-mens-road-running-shoes-mVJdmS/DV3853-004'


response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string

    product_name = soup.find('h1', class_='headline-2 css-16cqcdq').text
    price = soup.find('div', class_='product-price css-11s12ax is--current-price css-tpaepq').text

    print(f'Title: {title}')
    print(f'Product Name: {product_name}')
    print(f'Price: {price}')

else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
