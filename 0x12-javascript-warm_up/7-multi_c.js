#!/usr/bin/node

const args = process.argv;

const count = Number(args[2]);

if (isNaN(count) === true || !args[2]) {
  console.log('Missing number of occurrences');
  process.exit();
}

let iter = 0;

while (iter < count) {
  console.log('C is fun');
  iter = iter + 1;
}
