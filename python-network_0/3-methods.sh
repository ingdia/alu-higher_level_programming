#!/bin/bash
# This script takes a URL as an argument and displays all HTTP methods the server will accept
curl -s -X OPTIONS "$1" -i | grep "Allow:" | cut -d " " -f 2-
