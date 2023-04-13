#!/usr/bin/node

const args = process.argv[2];
if (!isNaN(args) || parseInt(args) === args) {
  console.log(`My number: ${parseInt(args)}`);
} else {
  console.log('Not a number');
}
