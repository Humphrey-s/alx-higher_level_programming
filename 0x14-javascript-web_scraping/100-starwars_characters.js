#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/';
const id = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const people = JSON.parse(body).results;
  console.log(people);

  for (const character of people) {
    const films = character.films;

    for (const film of films) {
      if (film.include(id)) {
        console.log(character.name);
      }
      console.log(film);
    }
  }
});
