#!/usr/bin/node

let bigNum = 0;
let sBigNum = 0;
for (let i = 2; i < process.argv.length; i++) {
  const num = Number(process.argv[i]);
  if (num > bigNum) {
    sBigNum = bigNum;
    bigNum = num;
  } else if (num > sBigNum && num < bigNum) {
    sBigNum = num;
  }
}
console.log(sBigNum);
