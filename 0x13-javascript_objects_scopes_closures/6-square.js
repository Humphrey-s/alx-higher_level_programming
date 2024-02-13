#!/usr/bin/node
Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let h = 0;
    let w;
    let square;
    let charP = 'X';

    if (typeof (c) !== 'undefined') {
      charP = 'C';
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
