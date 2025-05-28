#!/usr/bin/node
const request = require('request');

// Get the Movie ID from command-line arguments
const movieId = process.argv[2];

// Check if Movie ID is provided
if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

// SWAPI URL for the specified movie
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch movie data
request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  // Parse the response body
  let movieData;
  try {
    movieData = JSON.parse(body);
  } catch (parseError) {
    console.error('Error parsing movie data:', parseError);
    return;
  }

  // Check if the movie exists
  if (movieData.detail === 'Not found') {
    console.error('Movie not found');
    return;
  }

  // Get the list of character URLs
  const characters = movieData.characters;

  // Function to fetch and print character names in order
  const fetchCharacter = (index) => {
    if (index >= characters.length) {
      return; // All characters processed
    }

    request(characters[index], (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character data:', charError);
        return;
      }

      let charData;
      try {
        charData = JSON.parse(charBody);
      } catch (parseError) {
        console.error('Error parsing character data:', parseError);
        return;
      }

      // Print character name
      console.log(charData.name);

      // Fetch the next character
      fetchCharacter(index + 1);
    });
  };

  // Start fetching characters from index 0
  fetchCharacter(0);
});
