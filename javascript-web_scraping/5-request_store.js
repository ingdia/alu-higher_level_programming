#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get URL and file path from arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Perform GET request
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Write body to file in UTF-8
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
