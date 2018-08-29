#!/usr/bin/node
/* Prints "C is fun" x times, x is first argument passed in */
const firstArg = parseInt(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    let str = '';
    for (let j = 0; j < firstArg; j++) {
      str = str + 'X';
    }
    console.log(str);
  }
}
