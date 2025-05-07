""" Model Definitions for the application """
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Transaction:
    hash: str
    timestamp: datetime
    from_address: str
    to_address: str
    category: str            # E.g., ETH, BTC, ERC20, INTERNAL, etc.
    asset_contract: Optional[str]
    symbol: Optional[str]
    token_id: Optional[str]
    value: float
    fee: float    