#!/usr/bin/python3
"""
2-post_email.py

This script takes a URL and an email as arguments, sends a POST request
to the URL with the email as a parameter, and displays the body of the
response (decoded in utf-8).
"""

import urllib.request
import sys

if __name__ == "__main__":
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    data = f"email={email}".encode('utf-8')

    # Create a request object
    request = urllib.request.Request(url, data=data, method='POST')

    # Send the request and handle the response
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print(body.decode('utf-8'))
