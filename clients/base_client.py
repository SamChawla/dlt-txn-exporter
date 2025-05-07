"""This module provides the base client for interacting with the API."""
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class CryptoClient(ABC):
    @abstractmethod
    def fetch_transactions(self, address: str, **kwargs) -> List[Dict[str, Any]]:
        """Fetch on-chain transactions for the address."""
        pass

    @abstractmethod
    def fetch_internal_transactions(self, address: str, **kwargs) -> List[Dict[str, Any]]:
        """Fetch internal or contract-triggered transfers."""
        pass

    @abstractmethod
    def fetch_token_transfers(self, address: str, **kwargs) -> List[Dict[str, Any]]:
        """Fetch token or asset transfers."""
        pass