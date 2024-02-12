#!/usr/bin/node

const args = process.argv;
let count = 0;

for (const argv of args) {
  if (!args[2]) {
    console.log('No argument');
    break;
  }
  if (count > 1) {
    console.log(argv);
  }
  count = count + 1;
}
