#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else if (n < 0) {
    return -1;
  } else {
    return n * factorial(n - 1);
  }
}
const input = Number(process.argv[2]);
console.log(`factorial: ${factorial(input)}`);
