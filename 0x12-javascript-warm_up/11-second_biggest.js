#!/usr/bin/node

const args = (process.argv.slice(2).map(Number);

const totalArgs = args.length;
if (totalArgs <= 3) {
  console.log('0');
} else {
  let biggest = args[0];
  let secondBiggest = args[1];

  if (secondBiggest > biggest) {
    [biggest, secondBiggest] = [secondBiggest, biggest];
  }

  let i = 2;
  for (; i < totalArgs; i++) {
    const current = args[i];
    if (current > biggest) {
      secondBiggest = biggest;
      biggest = current;
    } else if (current > secondBiggest) {
      secondBiggest = current;
    }
  }
  console.log(secondBiggest);
}
