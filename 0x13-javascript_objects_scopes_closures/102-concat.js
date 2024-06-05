#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
    return;
  }
  fs.appendFileSync(fileC, data);

  fs.readFile(fileB, 'utf-8', function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    fs.appendFileSync(fileC, data);
  });
});
