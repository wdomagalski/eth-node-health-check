# eth-node-health-check

Small Python script that prints a few basic system stats and can optionally check an Ethereum RPC endpoint.

I mainly wrote it to practice and to have a small public project on GitHub.

## What it does

- shows CPU %
- shows RAM %
- shows disk usage
- pings a host (default: 8.8.8.8)
- optional: sends a simple `eth_blockNumber` request to an Ethereum RPC URL

## How to run

```bash
pip install -r requirements.txt
python3 check.py --host 8.8.8.8 --rpc https://cloudflare-eth.com
```

Or without RPC:

```bash
python3 check.py
```

## Docker

```bash
docker build -t node-health .
docker run -–rm node-health
```
