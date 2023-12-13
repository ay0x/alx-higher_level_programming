#!/usr/bin/node

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const character = c || 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = Square;
