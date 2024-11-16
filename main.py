import requests
from bs4 import BeautifulSoup
from email_service import EmailService

#URLs del producto
# Lista de productos
products = [
    {"name": "Juego de la vida", "url": "https://www.mercadolibre.com.ar/toyco-juego-de-la-vida-life/p/MLA15904269", "target_price": 39901.00},
    {"name": "Play station 5", "url": "https://www.mercadolibre.com.ar/sony-playstation-5-825gb-god-of-war-ragnarok-bundle-color-blanconegro/p/MLA19917557", "target_price": 10000000.00},
]
TARGET_PRICE = 39901.00  # Precio objetivo

from config import RECIPENT_EMAIL 

# Crea una instancia del servicio de correo
email_service = EmailService()

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


def track_prices(products):
    for product in products:
        try:
            title, price = get_product_price(product["url"])
            print(f"Producto: {title} | Precio actual: ${price}")

            # Verifica si el precio está por debajo del objetivo
            if price <= product["target_price"]:
                body = (
                    f"¡El precio del producto '{title}' ha bajado a ${price}!\n"
                    f"Link: {product['url']}"
                )
                email_service.send_email(
                    f"Alerta de precio bajo: {title}", body, recipient_email=RECIPENT_EMAIL
                )
        except Exception as e:
            print(f"Error rastreando {product['name']}: {e}")

track_prices(products)