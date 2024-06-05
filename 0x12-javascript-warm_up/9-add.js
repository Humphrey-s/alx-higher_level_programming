#!/usr/bin/node

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

function add (a, b) {
  if (isNaN(a) === true || isNaN(b) === true) {
    console.log(NaN);
    return false;
  }
  console.log(a + b);
  return a + b;
}

add(a, b);
