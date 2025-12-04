import psutil
import subprocess
import time
import argparse
import requests

def cpu():
    return psutil.cpu_percent(interval=1)

def memory():
    return psutil.virtual_memory().percent

def disk():
    return psutil.disk_usage('/').percent

def ping(host):
    try:
        start = time.time()
        subprocess.check_output(["ping", "-c", "1", host], stderr=subprocess.STDOUT)
        end = time.time()
        return round((end - start) * 1000, 2)
    except:
        return None

def rpc_check(url):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }

    try:
        r = requests.post(url, json=payload, timeout=3)
        data = r.json()

        # If RPC returned an error, just fail quietly
        if "error" in data:
            print("RPC error:", data["error"].get("message"))
            return False

        return "result" in data

    except requests.exceptions.RequestException:
        return False
    except ValueError:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rpc", help="Ethereum RPC URL")
    parser.add_argument("--host", default="8.8.8.8", help="Host to ping")
    args = parser.parse_args()

    print("CPU:", cpu(), "%")
    print("Memory:", memory(), "%")
    print("Disk:", disk(), "%")

    latency = ping(args.host)
    print("Ping to", args.host + ":", latency, "ms" if latency else "failed")

    if args.rpc:
        ok = rpc_check(args.rpc)
        print("RPC check:", "OK" if ok else "FAIL")