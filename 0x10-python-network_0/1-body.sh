#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
echo "$(curl -i -s http://$1 | head -1)"
