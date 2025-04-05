#!/bin/bash
# This script takes a URL as an argument and displays the body of the response only if the status code is 200
curl -s -o response_body.txt -w "%{http_code}" "$1" | grep -q "200" && cat response_body.txt
