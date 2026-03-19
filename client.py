
from binance.client import Client
import os
from dotenv import load_dotenv
from pathlib import Path

# 👇 FORCE correct path
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)


def get_client():
    return Client(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET"),
        testnet=True
    )