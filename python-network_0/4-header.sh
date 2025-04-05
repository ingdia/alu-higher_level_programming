#!/bin/bash
# Sends a GET request to the URL with header X-HolbertonSchool-User-Id: 98 and displays the body of the response
curl -sG "$1" -H "X-School-User-Id: 98"
