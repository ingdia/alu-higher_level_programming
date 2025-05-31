#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const nums = [];

  for (let i = 0; i < args.length; i++) {
    nums.push(parseInt(args[i]));
  }

  nums.sort(function (a, b) {
    return b - a;
  });

  console.log(nums[1]);
}
