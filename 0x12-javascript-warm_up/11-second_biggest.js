#!/usr/bin/node

const argv = process.argv;
let fArg = Number(argv[2]);

if (isNaN(fArg) === true || isNaN(argv[3]) === true) {
  console.log(0);
  process.exit();
}
let i = 2;

while (i < Number(argv.length)) {
  if (fArg < Number(argv[i])) {
    fArg = Number(argv[i]);
  }
  i++;
}

console.log(fArg);
