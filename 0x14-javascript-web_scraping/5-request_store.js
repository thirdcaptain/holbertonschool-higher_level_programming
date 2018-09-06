#!/usr/bin/node
// Gets content of a page and stores it in a file
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.appendFile(filename, body, function (err) {
      if (err) {
        return console.log(err);
      }
    });
  }
});
