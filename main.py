"""This is the main entry point for the application."""

import argparse
import logging
from clients.ethereum_client import EthereumClient
from processors.ethereum_processor import EthereumProcessor
from exporter import CSVExporter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CLIENTS = {
    'ethereum': (EthereumClient, EthereumProcessor),
}

def main():
    parser = argparse.ArgumentParser(description="Export blockchain transactions to CSV")
    parser.add_argument("address", help="Wallet address")
    parser.add_argument("outfile", help="CSV output file path")
    parser.add_argument("--chain", choices=CLIENTS.keys(), default="ethereum")
    args = parser.parse_args()

    client_cls, proc_cls = CLIENTS[args.chain]
    client = client_cls()
    processor = proc_cls()

    logger.info("Fetching on-chain txs...")
    raw_normal = client.fetch_transactions(args.address)
    raw_internal = client.fetch_internal_transactions(args.address)
    raw_token = client.fetch_token_transfers(args.address)

    logger.info("Processing transactions...")
    txs = []
    txs.extend(processor.process(raw_normal))
    txs.extend(processor.process(raw_internal))
    txs.extend(processor.process(raw_token))
    txs.sort(key=lambda x: x.timestamp)

    exporter = CSVExporter(args.outfile)
    exporter.export(txs)
    logger.info("Done! Saved to %s", args.outfile)

    logger.info("Exported %d transactions", len(txs))


if __name__ == '__main__':
    main()
