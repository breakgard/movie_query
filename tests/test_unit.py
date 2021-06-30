import movie_query.api
import movie_query.config
import movie_query.main
import movie_query.exceptions

import pytest
import requests
import json

mock_response_OK = json.dumps({"Title":"Test","Year":"2013","Rated":"TV-MA","Released":"04 Apr 2014","Runtime":"89 min","Genre":"Drama","Director":"Chris Mason Johnson","Writer":"Chris Mason Johnson","Actors":"Scott Marlowe, Matthew Risch, Evan Boomer","Plot":"San Francisco, 1985: Frankie confronts the challenges of being an understudy in a modern dance company as he embarks on a budding relationship with Todd, a veteran dancer in the same company and the bad boy to Frankie's innocent. As Frankie and Todd's friendship deepens, they navigate a world of risk - it's the early years of the epidemic - but also a world of hope, humor, visual beauty and musical relief.","Language":"English, Portuguese, French","Country":"United States","Awards":"3 wins & 3 nominations","Poster":"https://m.media-amazon.com/images/M/MV5BMTQwMDU5NDkxNF5BMl5BanBnXkFtZTcwMjk5OTk4OQ@@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.5/10"},{"Source":"Rotten Tomatoes","Value":"82%"},{"Source":"Metacritic","Value":"70/100"}],"Metascore":"70","imdbRating":"6.5","imdbVotes":"1,506","imdbID":"tt2407380","Type":"movie","DVD":"10 Aug 2016","BoxOffice":"$18,823","Production":"Serious Productions","Website":"N/A","Response":"True"})
mock_response_NOK = json.dumps({"Response":"False","Error":"Incorrect IMDb ID."})
mock_response_MOVIE_NOT_FOUND = json.dumps({"Response":"False","Error":"Movie not found!"})
mock_response_NOK_API_KEY = json.dumps({"Response":"False","Error":"Invalid API key!"})
mock_response_MISSING_API_KEY = json.dumps({"Response":"False","Error":"No API key provided."})
mock_response_NO_RATING = json.dumps({"Title":"Test","Year":"2013","Rated":"TV-MA","Released":"04 Apr 2014","Runtime":"89 min","Genre":"Drama","Director":"Chris Mason Johnson","Writer":"Chris Mason Johnson","Actors":"Scott Marlowe, Matthew Risch, Evan Boomer","Plot":"San Francisco, 1985: Frankie confronts the challenges of being an understudy in a modern dance company as he embarks on a budding relationship with Todd, a veteran dancer in the same company and the bad boy to Frankie's innocent. As Frankie and Todd's friendship deepens, they navigate a world of risk - it's the early years of the epidemic - but also a world of hope, humor, visual beauty and musical relief.","Language":"English, Portuguese, French","Country":"United States","Awards":"3 wins & 3 nominations","Poster":"https://m.media-amazon.com/images/M/MV5BMTQwMDU5NDkxNF5BMl5BanBnXkFtZTcwMjk5OTk4OQ@@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.5/10"},{"Source":"Metacritic","Value":"70/100"}],"Metascore":"70","imdbRating":"6.5","imdbVotes":"1,506","imdbID":"tt2407380","Type":"movie","DVD":"10 Aug 2016","BoxOffice":"$18,823","Production":"Serious Productions","Website":"N/A","Response":"True"})

mock_API_KEY="12345asdfg"
mock_TITLE="Test"

def test_check_api_key_OK(requests_mock):
  requests_mock.get(movie_query.config.API_URL, status_code=200, text=mock_response_OK)
  movie_query.api.check_api_key(movie_query.config.API_URL, mock_API_KEY)

def test_check_api_key_NOK(requests_mock):
  requests_mock.get(movie_query.config.API_URL, status_code=401, text=mock_response_NOK_API_KEY)
  with pytest.raises(Exception):
    movie_query.api.check_api_key(movie_query.config.API_URL, mock_API_KEY)

def test_check_api_key_MISSING_API_KEY(requests_mock):
  requests_mock.get(movie_query.config.API_URL, status_code=401, text=mock_response_MISSING_API_KEY)
  with pytest.raises(Exception):
    movie_query.api.check_api_key(movie_query.config.API_URL, "")

def test_query_by_title_OK(requests_mock):
  requests_mock.get(movie_query.config.API_URL, status_code=200, text=mock_response_OK)
  assert json.loads(mock_response_OK) == movie_query.api.query_by_title(movie_query.config.API_URL, mock_API_KEY, mock_TITLE)

def test_query_by_title_NOK(requests_mock):
  requests_mock.get(movie_query.config.API_URL, status_code=200, text=mock_response_NOK)
  assert json.loads(mock_response_NOK) == movie_query.api.query_by_title(movie_query.config.API_URL, mock_API_KEY, mock_TITLE)

def test_get_movie_rating_OK(requests_mock):
  requests_mock.get(movie_query.config.API_URL, status_code=200, text=mock_response_OK)
  assert "82%" == movie_query.main.get_movie_rating(movie_query.config.API_URL, mock_API_KEY, mock_TITLE, movie_query.config.RATING_SOURCE)

def test_get_movie_rating_OK_NO_RATING(requests_mock):
  requests_mock.get(movie_query.config.API_URL, status_code=200, text=mock_response_NO_RATING)
  assert "N/A" == movie_query.main.get_movie_rating(movie_query.config.API_URL, mock_API_KEY, mock_TITLE, movie_query.config.RATING_SOURCE)

def test_get_movie_rating_NOK(requests_mock):
  requests_mock.get(movie_query.config.API_URL, status_code=200, text=mock_response_MOVIE_NOT_FOUND)
  with pytest.raises(movie_query.exceptions.MovieNotFoundException):
    movie_query.main.get_movie_rating(movie_query.config.API_URL, mock_API_KEY, mock_TITLE, movie_query.config.RATING_SOURCE)
