#!/usr/bin/node
// Logs the number of arguments printed, and prints argument value
let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
