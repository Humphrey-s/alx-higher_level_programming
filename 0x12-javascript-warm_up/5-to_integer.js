#!/usr/bin/node

const args = process.argv;

if (!args[2]) {
  console.log('Not a number');
  process.exit();
}

if (isNaN(args[2]) !== true) {
  console.log(`My number: ${args[2]}`);
} else {
  console.log('Not a number');
}
