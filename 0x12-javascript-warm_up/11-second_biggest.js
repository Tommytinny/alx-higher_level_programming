#!/usr/bin/node

let bigNum = 0;
let sBigNum = 0;
for (let i = 2; i < process.argv.length; i++) {
  if (process.argv[i] > bigNum) {
    sBigNum = bigNum;
    bigNum = process.argv[i];
  } else if (process.argv[i] > sBigNum && process.argv[i] < bigNum) {
    sBigNum = process.argv[i];
  }
}
console.log(sBigNum);
