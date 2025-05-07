# DLT Transaction Exporter

## Overview

Export blockchain transactions to CSV with on-chain categorization

## Prerequisites

- Python 3.8+
- An Etherscan API Key (free-tier): sign up at https://etherscan.io/apis

## Installation

### Clone repository

```bash
git clone https://github.com/SamChawla/dlt-txn-exporter.git
cd dlt-txn-exporter
```

### Create & activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\\Scripts\\activate     # Windows PowerShell
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment

- Create a .env in the project root:

```text
ETHERSCAN_API_KEY=YOUR_KEY_HERE
ETHERSCAN_CHAIN_ID=1 # ETHERSCAN_CHAIN_ID defaults to 1 for Mainnet.
```

## Usage

```bash
python main.py <ADDRESS> <OUTFILE>
python main.py 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae  sample.csv
```

## Assumptions

- The user supplies a valid Etherscan API key with sufficient rate limits.
- Default chain is Ethereum Mainnet (chain ID 1).
- Transactions with non-empty input data are classified as Internal Transfers; otherwise External.
- Token transfers without a tokenID field are ERC-20, with tokenID are ERC-721.
- Gas usage and price fields (gasUsed, gasPrice) are always present for normal transactions.
- This prototype targets address-level exports; it does not maintain state or balances.

## Architecture Design

- Modular Client/Processor/Exporter
- Abstract Base Interfaces
- In-Memory Sorting
- Minimal Dependencies
