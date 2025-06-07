#!/usr/bin/node

const request = require('request');

// Get API URL from the command-line argument
const apiUrl = process.argv[2];
const characterId = '18';

// Send GET request to the films endpoint
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body).results;
  let count = 0;

  for (const film of data) {
    for (const characterUrl of film.characters) {
      if (characterUrl.includes(`/people/${characterId}/`)) {
        count++;
        break;
      }
    }
  }

  console.log(count);
});
