#!/usr/local/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

for (var index = 0; index < 100; index++) {
    console.log(myConverter(index));
}
