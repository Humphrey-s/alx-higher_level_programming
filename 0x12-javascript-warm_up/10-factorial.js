#!/usr/bin/node

function factorial (a) {
  if (isNaN(a) === true || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const a = Number(process.argv[2]);

console.log(factorial(a));
