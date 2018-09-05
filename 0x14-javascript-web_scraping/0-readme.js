#!/usr/bin/node
// Reads and prints contents of a file
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (err, contents) {
  if (err) {
    return console.error(err);
  }
  console.log(contents);
});
