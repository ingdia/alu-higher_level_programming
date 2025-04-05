#!/usr/bin/python3
"""
1-hbtn_header.py

This script takes a URL as an argument, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the
header of the response.
"""

import urllib.request
import sys

def fetch_x_request_id(url):
    """Fetches the X-Request-Id from the response header."""
    with urllib.request.urlopen(url) as response:
        # Get the value of the X-Request-Id header
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

if __name__ == "__main__":
    # Get the URL from the command line arguments
    url = sys.argv[1]
    fetch_x_request_id(url)
