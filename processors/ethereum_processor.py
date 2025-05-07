""" This module provides functionality for processing Ethereum transactions. """

from datetime import datetime
from decimal import Decimal
from typing import List
from .base_processor import BaseProcessor
from models import Transaction

class EthereumProcessor(BaseProcessor):
    @staticmethod
    def _timestamp(ts: str) -> datetime:
        return datetime.fromtimestamp(int(ts))

    @staticmethod
    def _to_decimal(amount: str, decimals: int) -> float:
        return float(Decimal(amount) / Decimal(10**decimals))

    def process(self, raw: List[dict]) -> List[Transaction]:
        txs: List[Transaction] = []
        for r in raw:
            try:
                fee = 0.0
                if r.get("gasUsed") and r.get("gasPrice"):
                    fee = self._to_decimal(str(int(r["gasUsed"]) * int(r["gasPrice"])), 18)
                value = self._to_decimal(r.get("value", "0"), 18)
                tx = Transaction(
                    hash=r.get("hash"),
                    timestamp=self._timestamp(r.get("timeStamp")),
                    from_address=r.get("from"),
                    to_address=r.get("to"),
                    category="Internal Transfer" if (r.get("input") or "") != "0x" else "External Transfer",
                    asset_contract=None,
                    symbol="ETH",
                    token_id=None,
                    value=value,
                    fee=fee
                )
                txs.append(tx)
            except Exception:
                continue
        return txs