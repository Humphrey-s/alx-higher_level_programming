#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const content = JSON.parse(body);
  const films = content.results;
  let count = 0;

  for (const film of films) {
    const filmCharacters = film.characters;

    for (const character of filmCharacters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
