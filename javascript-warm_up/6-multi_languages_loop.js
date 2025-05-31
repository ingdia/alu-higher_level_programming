#!/usr/bin/node

const arg = process.argv.slice(2);
let i = 0;
while (i < arg.length) {
  console.log(arg[i]);
  i++;
}
