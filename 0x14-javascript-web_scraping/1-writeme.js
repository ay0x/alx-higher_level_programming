#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const text = process.argv[3];
const encoding = 'utf-8';

if (!filePath) {
  console.error('Provide a file path as the first argument');
}

fs.writeFile(filePath, text, encoding, (err, data) => {
  if (err) {
    console.error(err);
  }
});
