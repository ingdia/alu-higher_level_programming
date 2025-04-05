#!/usr/bin/python3
import urllib.request

# Fetch the URL
with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    body = response.read()

# Display the response in the required format
print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: {body.decode('utf-8')}")
