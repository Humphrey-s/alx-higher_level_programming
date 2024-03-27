#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = body;

  fs.writeFile(file, data, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
