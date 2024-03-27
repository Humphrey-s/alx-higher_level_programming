#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const content = JSON.parse(body);
  const films = content.results;

  for (const film of films) {
    if (film.url.includes(id)) {
      const characters = film.characters;

      for (let i = 0; i < characters.length; i++) {
        request(characters[i], function (error, response, body) {
          if (error) {
            console.error(error);
          }
          const name = JSON.parse(body).name;
          console.log(name);
        });
      }
    }
  }
});
