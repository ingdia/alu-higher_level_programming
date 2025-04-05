#!/usr/bin/python3
"""
0-hbtn_status.py

This script fetches the status from the URL 'https://alu-intranet.hbtn.io/status'
and displays the response body in a formatted manner. It uses the urllib package
to make the HTTP request and handle the response.

Usage:
    Run the script directly to see the output.

Expected Output:
    The script will print the type of the response, the raw content, and the UTF-8
    decoded content of the response.
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
