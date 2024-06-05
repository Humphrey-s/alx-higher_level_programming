#!/usr/bin/node

exports.addMeMaybe = function addMeMaybe (number, thefunction) {
  number = number + 1;
  thefunction(number);
};
