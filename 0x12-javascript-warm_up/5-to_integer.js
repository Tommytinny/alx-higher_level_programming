#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (num) {
  const result = 'My number: ' + num;
  console.log(result);
} else {
  console.log('Not a number');
}
