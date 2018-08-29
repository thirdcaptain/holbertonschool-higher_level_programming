#!/usr/bin/node
/* Computes and prints a factorial */
const firstArg = parseInt(process.argv[2]);

function factorial (num) {
  if (num > 0) {
    return (num * factorial(num - 1));
  } else {
    return (1);
  }
}

console.log(factorial(firstArg));
