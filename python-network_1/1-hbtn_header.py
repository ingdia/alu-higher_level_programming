#!/usr/bin/python3
"""
0-hbtn_status.py

This script fetches the status from the URL https://alu-intranet.hbtn.io/status
and displays the response body, including the type, content, and UTF-8 content.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"

    # Use a with statement to open the URL
    with urllib.request.urlopen(url) as response:
        body = response.read()

    # Display the response details
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
