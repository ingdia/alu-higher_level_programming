#!/usr/bin/node

function reversemylist (list) {
  const reversedlist = [];
  for (let i = list.lenght - 1; i >= 0; i--) {
    reversedlist.push(list[i]);
  }
  return reversedlist;
}
module.exports = reversemylist;
