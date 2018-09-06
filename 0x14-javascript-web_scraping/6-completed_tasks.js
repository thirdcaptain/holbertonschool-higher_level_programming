#!/usr/bin/node
// computes the number of completed tasks
const request = require('request');
const url = process.argv[2];

let myJSON = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (let user of JSON.parse(body)) {
      if (user.completed === true) {
        if (!(user.userId in myJSON)) {
          myJSON[user.userId] = 1;
        } else {
          myJSON[user.userId] = myJSON[user.userId] + 1;
        }
      }
    }
  }
  console.log(myJSON);
});
