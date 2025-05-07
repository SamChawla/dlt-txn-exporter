"""This module provides an interface for interacting with the Ethereum blockchain."""

import requests
from typing import List, Dict, Any
from .base_client import CryptoClient
from config import settings

class EthereumClient(CryptoClient):
    """ Client for interacting with the Ethereum blockchain using Etherscan API. """

    def __init__(self):
        self.api_key = settings.ETHERSCAN_API_KEY
        self.base_url = settings.ETHERSCAN_BASE_URL
        self.timeout = settings.TIMEOUT
        if not self.api_key:
            raise ValueError("Missing Etherscan API key")

    def _get(self, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        print(self.api_key)
        params.update({"apikey": self.api_key, "chainId": settings.ETHERSCAN_CHAIN_ID})
        resp = requests.get(self.base_url, params=params, timeout=self.timeout)
        resp.raise_for_status()
        data = resp.json()
        if data.get("status") != "1":
            raise RuntimeError(f"Etherscan error: {data.get('message')}")
        return data.get("result", [])

    def fetch_transactions(self, address: str, **kwargs) -> List[Dict[str, Any]]:
        return self._get({"module": "account", "action": "txlist", "address": address, **kwargs})

    def fetch_internal_transactions(self, address: str, **kwargs) -> List[Dict[str, Any]]:
        return self._get({"module": "account", "action": "txlistinternal", "address": address, **kwargs})

    def fetch_token_transfers(self, address: str, **kwargs) -> List[Dict[str, Any]]:
        return self._get({"module": "account", "action": "tokentx", "address": address, **kwargs})
