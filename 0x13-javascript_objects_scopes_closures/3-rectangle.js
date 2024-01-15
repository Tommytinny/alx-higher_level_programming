#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let count = 0;
    while (count < this.height) {
      let row = '';
      for (let i = 0; i < this.width; i++) {
        row += 'X';
      }
      console.log(row);
      count++;
    }
  }
}

module.exports = Rectangle;
