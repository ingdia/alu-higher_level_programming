#!/usr/bin/python3
"""
3-error_code.py

This script takes a URL as a command-line argument, sends a request to the URL,
and displays the body of the response (decoded in UTF-8). If an HTTP error occurs,
it prints the error code.

Usage:
    ./3-error_code.py <URL>

Example:
    ./3-error_code.py http://0.0.0.0:5000
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # Get the URL from command line arguments
    url = sys.argv[1]

    try:
        # Send the request and handle the response
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        # Print the error code if an HTTP error occurs
        print(f"Error code: {e.code}")
