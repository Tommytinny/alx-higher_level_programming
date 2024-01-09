#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (size) {
  let count = 0;
  while (count < size) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
    count++;
  }
} else {
  console.log('Missing size');
}
