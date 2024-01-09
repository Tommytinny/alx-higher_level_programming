#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const int1 = parseInt(process.argv[2]);
const int2 = parseInt(process.argv[3]);
const result = add(int1, int2);
console.log(result);
