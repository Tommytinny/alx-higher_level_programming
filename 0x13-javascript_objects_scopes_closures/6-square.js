#!/usr/bin/node

const square = require('./5-square');
class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let count = 0;
      while (count < this.height) {
        let row = '';
        for (let i = 0; i < this.height; i++) {
          row += c;
        }
        console.log(row);
        count++;
      }
    }
  }
}

module.exports = Square;
