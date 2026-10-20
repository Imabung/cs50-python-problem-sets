
import os
import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_key = os.getenv("COINCAP_API_KEY")
    url = "https://rest.coincap.io/v3/assets/bitcoin"

    try:
        response = requests.get(
            url,
            params={"apiKey": api_key},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except (requests.RequestException, KeyError, TypeError, ValueError):
        sys.exit("Could not retrieve Bitcoin price")

    total = bitcoins * price
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
