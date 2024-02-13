#!/usr/bin/node

exports.esrever = function (list) {
  if (!list) {
    return;
  }
  let length = list.length;
  const revList = [];
  let iter = 0;

  while (length > 0) {
    revList[iter] = list[length - 1];
    iter = iter + 1;
    length = length - 1;
  }
  return (revList);
};
