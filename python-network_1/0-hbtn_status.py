#!/usr/bin/python3
"""
This script fetches the status from the specified URL
and displays the response body in a formatted manner.
"""

import urllib.request

def fetch_status():
    """Fetches the status from the URL and prints the response."""
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
        body = response.read()

    # Display the response in the required format
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()
