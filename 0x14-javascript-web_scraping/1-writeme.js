#!/usr/bin/node
// Reads and writes a string to a file
const fs = require('fs');
fs.appendFile(process.argv[2], process.argv[3], function (err) {
  if (err) {
    return console.log(err);
  }
});
