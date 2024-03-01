#!/bin/bash
#  Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -i -sL -X OPTIONS $1 | grep "Allow: " | cut -b 8-20
