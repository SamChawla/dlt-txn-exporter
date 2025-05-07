"""This module handles the export functionality for the application."""

import csv
from typing import List
from models import Transaction

class CSVExporter:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def export(self, txs: List[Transaction]) -> None:
        header = [
            "Transaction Hash", "Date & Time", "From Address", "To Address",
            "Type", "Contract", "Symbol", "Token ID", "Value", "Fee"
        ]
        with open(self.filepath, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for tx in txs:
                writer.writerow([
                    tx.hash,
                    tx.timestamp.isoformat(),
                    tx.from_address,
                    tx.to_address,
                    tx.category,
                    tx.asset_contract or "",
                    tx.symbol or "",
                    tx.token_id or "",
                    tx.value,
                    tx.fee
                ])