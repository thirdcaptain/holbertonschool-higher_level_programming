#!/usr/bin/node
// Rectangle class with constructor and print method
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Prints the rectangle using X
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    // Doubles the width and the height of rectangle
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    // Exchanges the values of width and height
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

module.exports = Rectangle;
