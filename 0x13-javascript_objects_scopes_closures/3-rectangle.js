#!/usr/bin/node.js

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let h = 0;
    let w;
    let rectangle;

    while (h < this.height) {
      w = 0;
      rectangle = '';
      while (w < this.width) {
        rectangle = rectangle + 'X';
        w = w + 1;
      }
      console.log(rectangle);
      h = h + 1;
    }
  }
}

module.exports = Rectangle;
