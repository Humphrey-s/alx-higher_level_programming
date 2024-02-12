#!/usr/bin/node

const args = process.argv;
let it = 0;

while (it <= 5) {
  if (!args[it]) {
    break;
  }

  it = it + 1;
}

if (it === 3) {
  console.log('Argument found');
} else {
  if (it > 3) {
    console.log('Arguments found');
  } else {
    console.log('No Argument');
  }
}
