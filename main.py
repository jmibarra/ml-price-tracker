import requests
from bs4 import BeautifulSoup

#URL del producto
URL = 'https://www.mercadolibre.com.ar/toyco-juego-de-la-vida-life/p/MLA15904269'
TARGET_PRICE = 39901.00  # Precio objetivo

# Cabeceras para imitar un navegador real
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def get_product_price(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    #Extraigo el título del producto
    title = soup.find('h1', {'class': 'ui-pdp-title'}).text.strip()

    #Extraigo el precio del producto
    price = soup.find('span', {'class': 'andes-money-amount__fraction'}).get_text(strip=True).replace('.', '')
    price = float(price)  # Convertir a número

    return title, price

def check_price(title, price):
    if price < TARGET_PRICE:
        print(f"¡El precio del producto '{title}' ha bajado a ${price}!")
    else:
        print(f"El precio sigue alto (${price}).")

title, price = get_product_price(URL)
check_price(title, price)