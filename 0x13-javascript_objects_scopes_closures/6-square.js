#!/usr/bin/node
Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let h = 0;
    let w;
    let square;
    let charP = c;

    if (typeof (c) === 'undefined') {
      charP = 'X';
    }
    while (h < this.size) {
      w = 0;
      square = '';
      while (w < this.size) {
        square = square + charP;
        w = w + 1;
      }
      console.log(square);
      h = h + 1;
    }
  }
}
module.exports = Square;
