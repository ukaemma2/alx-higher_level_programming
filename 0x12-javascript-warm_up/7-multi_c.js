#!/usr/bin/node
const args = process.argv.slice(2);
/* Extracting the arguments passed to the script */
const x = parseInt(args[0]);
/* Parse first argument as integer */
let i = 0;

if (isNaN(x)) {
  console.log('Mission number of occurrences');
  /* print error if the argument is not a number */
} else {
  for (; i < x; i++) {
    console.log('C is fun');
  }
}
