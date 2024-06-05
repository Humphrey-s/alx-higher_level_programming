#!/usr/bin/node
const dict = require('./101-data').dict;
const newDct = {};
const keys = [];
for (const key in dict) {
  keys.push(dict[key]);
}

keys.forEach(function (key) {
  const array = [];
  for (const a in dict) {
    if (dict[a] === key) {
      array.push(a);
    }
  }

  newDct[key] = array;
});

console.log(newDct);
