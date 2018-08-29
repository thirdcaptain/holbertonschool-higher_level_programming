#!/usr/bin/node
/* Returns second biggest integer in list */
const arrLen = process.argv.length;
let arrNums = [];

if (arrLen < 4) {
  console.log(0);
} else {
  for (let i = 2; i < arrLen; i++) {
    arrNums.push(parseInt(process.argv[i]));
  }
  arrNums.sort();
  console.log(arrNums[arrLen - 4]);
}
