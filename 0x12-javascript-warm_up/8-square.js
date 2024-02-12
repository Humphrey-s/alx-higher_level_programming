#!/usr/bin/node

const args = process.argv;

const size = Number(args[2]);

if (!size || isNaN(size) === true) {
  console.log('Missing size');
  process.exit();
}

let height = 0;
let wSize = '';

while (height < size) {
  let width = 0;
  while (width < size) {
    wSize = wSize + 'X';
    width = width + 1;
  }
  if (height + 1 !== size) {
    wSize = wSize + '\n';
  }
  height = height + 1;
}

console.log(wSize);
