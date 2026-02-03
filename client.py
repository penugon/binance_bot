import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_authenticated_client() -> Client:
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise EnvironmentError("API keys not found in .env")

    client = Client(
        api_key=api_key,
        api_secret=api_secret,
        testnet=True
    )

    # Ensure futures endpoint uses testnet
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client
