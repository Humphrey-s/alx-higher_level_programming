#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  if (!list) {
    return;
  }
  let num = 0;
  for (const element of list) {
    if (searchElement === element) {
      num = num + 1;
    }
  }
  return (num);
};
