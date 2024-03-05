#!/bin/bash
#  Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message
curl -s -X POST -d "body=You got me!" $1
