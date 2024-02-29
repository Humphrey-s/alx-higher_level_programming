#!/usr/bin/env bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ "$#" -ne 1 ];
then
	exit;
fi

url=$(curl -s http://$1)
size=${#url}

echo "$size"
