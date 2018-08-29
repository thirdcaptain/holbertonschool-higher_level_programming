#!/usr/bin/node
/* Convert the first argument to an integer */
const firstArg = process.argv[2];
if (isNaN(Number(firstArg))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(firstArg));
}
