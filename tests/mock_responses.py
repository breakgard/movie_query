"""Contains all mock responses used in tests."""

import json

mock_response_OK = json.dumps(
    {
        "Title": "Test",
        "Year": "2013",
        "Rated": "TV-MA",
        "Released": "04 Apr 2014",
        "Runtime": "89 min",
        "Genre": "Drama",
        "Director": "Chris Mason Johnson",
        "Writer": "Chris Mason Johnson",
        "Actors": "Scott Marlowe, Matthew Risch, Evan Boomer",
        "Plot": "San Francisco, 1985: Frankie confronts the challenges of being an understudy in a modern dance company as he embarks on a budding relationship with Todd, a veteran dancer in the same company and the bad boy to Frankie's innocent. As Frankie and Todd's friendship deepens, they navigate a world of risk - it's the early years of the epidemic - but also a world of hope, humor, visual beauty and musical relief.",
        "Language": "English, Portuguese, French",
        "Country": "United States",
        "Awards": "3 wins & 3 nominations",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMTQwMDU5NDkxNF5BMl5BanBnXkFtZTcwMjk5OTk4OQ@@._V1_SX300.jpg",
        "Ratings": [
            {"Source": "Internet Movie Database", "Value": "6.5/10"},
            {"Source": "Rotten Tomatoes", "Value": "82%"},
            {"Source": "Metacritic", "Value": "70/100"},
        ],
        "Metascore": "70",
        "imdbRating": "6.5",
        "imdbVotes": "1,506",
        "imdbID": "tt2407380",
        "Type": "movie",
        "DVD": "10 Aug 2016",
        "BoxOffice": "$18,823",
        "Production": "Serious Productions",
        "Website": "N/A",
        "Response": "True",
    }
)
mock_response_NOK = json.dumps({"Response": "False", "Error": "Incorrect IMDb ID."})
mock_response_MOVIE_NOT_FOUND = json.dumps(
    {"Response": "False", "Error": "Movie not found!"}
)
mock_response_NOK_API_KEY = json.dumps(
    {"Response": "False", "Error": "Invalid API key!"}
)
mock_response_MISSING_API_KEY = json.dumps(
    {"Response": "False", "Error": "No API key provided."}
)
mock_response_NO_RATING = json.dumps(
    {
        "Title": "Test",
        "Year": "2013",
        "Rated": "TV-MA",
        "Released": "04 Apr 2014",
        "Runtime": "89 min",
        "Genre": "Drama",
        "Director": "Chris Mason Johnson",
        "Writer": "Chris Mason Johnson",
        "Actors": "Scott Marlowe, Matthew Risch, Evan Boomer",
        "Plot": "San Francisco, 1985: Frankie confronts the challenges of being an understudy in a modern dance company as he embarks on a budding relationship with Todd, a veteran dancer in the same company and the bad boy to Frankie's innocent. As Frankie and Todd's friendship deepens, they navigate a world of risk - it's the early years of the epidemic - but also a world of hope, humor, visual beauty and musical relief.",
        "Language": "English, Portuguese, French",
        "Country": "United States",
        "Awards": "3 wins & 3 nominations",
        "Poster": "https://m.media-amazon.com/images/M/MV5BMTQwMDU5NDkxNF5BMl5BanBnXkFtZTcwMjk5OTk4OQ@@._V1_SX300.jpg",
        "Ratings": [
            {"Source": "Internet Movie Database", "Value": "6.5/10"},
            {"Source": "Metacritic", "Value": "70/100"},
        ],
        "Metascore": "70",
        "imdbRating": "6.5",
        "imdbVotes": "1,506",
        "imdbID": "tt2407380",
        "Type": "movie",
        "DVD": "10 Aug 2016",
        "BoxOffice": "$18,823",
        "Production": "Serious Productions",
        "Website": "N/A",
        "Response": "True",
    }
)
