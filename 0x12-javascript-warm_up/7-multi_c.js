#!/usr/bin/node
/* Prints "C is fun" x times, x is first argument passed in */
const firstArg = parseInt(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
}
