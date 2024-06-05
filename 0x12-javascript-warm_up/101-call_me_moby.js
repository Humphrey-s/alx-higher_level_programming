#!/usr/bin/node

exports.callMeMoby = function callMeMoby (a, func) {
  let i = 0;
  while (i < a) {
    func();
    i++;
  }
};
