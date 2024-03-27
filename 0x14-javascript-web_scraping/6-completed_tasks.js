#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let nUsers = 0;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }

  const tasks = JSON.parse(body);

  for (const task of tasks) {
    if (task.userId > nUsers) { nUsers = task.userId; }
  }
  let i = 1;
  const dict = {};

  while (i <= nUsers) {
    dict[i] = 0;
    i++;
  }

  i = 1;

  while (i <= nUsers) {
    for (const task of tasks) {
      if (task.userId === i) {
        if (task.completed === true) { dict[i]++; }
      }
    }
    i++;
  }
  console.log(dict);
});
