#!/bin/bash
#  Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message
curl -sL -X PUT --data-raw "You got me!" 0.0.0.0:5000/catch_me
