#!/usr/bin/node

const size = parseInt(process.argv[2]);

let i = 0;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (; i < size; i++) {
    let j = 0;
    let row = '';
    for (; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
