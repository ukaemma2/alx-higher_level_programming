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
<<<<<<< HEAD
console.log(`factorial: ${factorial(input)}`);
=======
console.log(`${factorial(input)}`);
>>>>>>> 1b7e0dc5de42dbdea8ec197b06879ee6444b4c8d
