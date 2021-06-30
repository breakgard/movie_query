"""Contains unit tests for movie_query package."""

import json
import pytest

import mock_responses

import movie_query.api
import movie_query.config
import movie_query.exceptions
import movie_query.main


MOCK_API_KEY = "12345asdfg"
MOCK_TITLE = "Test"


def test_check_api_key_ok(requests_mock):
    """Unit test"""
    requests_mock.get(
        movie_query.config.API_URL,
        status_code=200,
        text=mock_responses.mock_response_OK,
    )
    movie_query.api.check_api_key(movie_query.config.API_URL, MOCK_API_KEY)


def test_check_api_key_nok(requests_mock):
    """Unit test"""
    requests_mock.get(
        movie_query.config.API_URL,
        status_code=401,
        text=mock_responses.mock_response_NOK_API_KEY,
    )
    with pytest.raises(Exception):
        movie_query.api.check_api_key(movie_query.config.API_URL, MOCK_API_KEY)


def test_check_api_key_missing_api_key(requests_mock):
    """Unit test"""
    requests_mock.get(
        movie_query.config.API_URL,
        status_code=401,
        text=mock_responses.mock_response_MISSING_API_KEY,
    )
    with pytest.raises(Exception):
        movie_query.api.check_api_key(movie_query.config.API_URL, "")


def test_query_by_title_ok(requests_mock):
    """Unit test"""
    requests_mock.get(
        movie_query.config.API_URL,
        status_code=200,
        text=mock_responses.mock_response_OK,
    )
    assert json.loads(
        mock_responses.mock_response_OK
    ) == movie_query.api.query_by_title(
        movie_query.config.API_URL, MOCK_API_KEY, MOCK_TITLE
    )


def test_query_by_title_nok(requests_mock):
    """Unit test"""
    requests_mock.get(
        movie_query.config.API_URL,
        status_code=200,
        text=mock_responses.mock_response_NOK,
    )
    assert json.loads(
        mock_responses.mock_response_NOK
    ) == movie_query.api.query_by_title(
        movie_query.config.API_URL, MOCK_API_KEY, MOCK_TITLE
    )


def test_get_movie_rating_ok(requests_mock):
    """Unit test"""
    requests_mock.get(
        movie_query.config.API_URL,
        status_code=200,
        text=mock_responses.mock_response_OK,
    )
    assert (
        movie_query.main.get_movie_rating(
            movie_query.config.API_URL,
            MOCK_API_KEY,
            MOCK_TITLE,
            movie_query.config.RATING_SOURCE,
        )
        == "82%"
    )


def test_get_movie_rating_ok_no_rating(requests_mock):
    """Unit test"""
    requests_mock.get(
        movie_query.config.API_URL,
        status_code=200,
        text=mock_responses.mock_response_NO_RATING,
    )
    assert (
        movie_query.main.get_movie_rating(
            movie_query.config.API_URL,
            MOCK_API_KEY,
            MOCK_TITLE,
            movie_query.config.RATING_SOURCE,
        )
        == "N/A"
    )


def test_get_movie_rating_nok(requests_mock):
    """Unit test"""
    requests_mock.get(
        movie_query.config.API_URL,
        status_code=200,
        text=mock_responses.mock_response_MOVIE_NOT_FOUND,
    )
    with pytest.raises(movie_query.exceptions.MovieNotFoundException):
        movie_query.main.get_movie_rating(
            movie_query.config.API_URL,
            MOCK_API_KEY,
            MOCK_TITLE,
            movie_query.config.RATING_SOURCE,
        )
