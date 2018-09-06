#!/usr/bin/node
// Displays the number of movies where Wedge Angilles is present

let count = 0;
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].search('/18/') > 0) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
