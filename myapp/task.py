from celery import shared_task
import requests
from django.utils.timezone import now

@shared_task
def fetch_crypto_prices():
    """Fetch Bitcoin and Ethereum prices from CoinGecko API every 5 minutes."""
    from myapp.models import Organization, CryptoPrice 

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "bitcoin" in data and "ethereum" in data:
            btc_price = data["bitcoin"]["usd"]
            eth_price = data["ethereum"]["usd"]

            for org in Organization.objects.all():
                CryptoPrice.objects.create(
                    org=org, symbol="BTC", defaults={"price": btc_price, "timestamp": now()}
                )
                CryptoPrice.objects.create(
                    org=org, symbol="ETH", defaults={"price": eth_price, "timestamp": now()}
                )

            return f"BTC: ${btc_price}, ETH: ${eth_price} prices updated."

    except requests.exceptions.RequestException as e:
        return f"Error fetching crypto prices: {str(e)}"