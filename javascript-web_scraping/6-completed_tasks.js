#!/usr/bin/node

const request = require('request');

// Get URL from command-line argument
const url = process.argv[2];

// Send GET request
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasksByUser = {};

  for (const todo of todos) {
    if (todo.completed) {
      const userId = todo.userId;
      if (!completedTasksByUser[userId]) {
        completedTasksByUser[userId] = 1;
      } else {
        completedTasksByUser[userId]++;
      }
    }
  }

  console.log(completedTasksByUser);
});
