#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ "$#" -ne 1 ];
then
	exit;
fi

size=$(curl -s $1 | wc -c)

echo "$size"
