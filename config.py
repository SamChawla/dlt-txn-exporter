""" Settings for the application. """

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Configuration settings for the application."""
    ETHERSCAN_API_KEY: str = os.getenv("ETHERSCAN_API_KEY", "")
    ETHERSCAN_CHAIN_ID: int = int(os.getenv("ETHERSCAN_CHAIN_ID", 1))  # Default to Ethereum Mainnet
    ETHERSCAN_BASE_URL: str = "https://api.etherscan.io/v2/api"
    TIMEOUT: int = 10
   
settings = Settings()