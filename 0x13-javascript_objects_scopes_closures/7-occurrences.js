#!/usr/bin/node
// Function that returns the number of occurences in a list
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      counter++;
    }
  }
  return (counter);
};
