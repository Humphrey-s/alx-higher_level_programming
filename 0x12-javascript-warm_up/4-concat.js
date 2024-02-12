#!/usr/bin/node

const args = process.argv;

if (!args[2]) {
  console.log('undefined is undefined');
  process.exit(0);
}

if (!args[3]) {
  console.log(`${args[2]} is undefined`);
  process.exit(0);
}

console.log(`${args[2]} is ${args[3]}`);
