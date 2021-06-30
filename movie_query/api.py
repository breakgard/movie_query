"""API functions for querying Open movie database API."""

import logging
import requests

from . import config


def check_api_key(api_url, api_key, timeout=config.TIMEOUT):
    """Verifies if the api_key is valid."""

    logging.debug("Entering check_api_key")
    if api_key == "" or api_key is None:
        raise Exception("Api key not provided.")
    params = {"apikey": api_key}
    result = requests.get(api_url, params=params, timeout=timeout)
    logging.debug(f"Result: {result.text}")
    if result.status_code != 200:
        if result.status_code == 401:
            raise Exception("Api key is invalid.")
        else:
            raise Exception(f"Error when connecting to API: {result.text}")
    logging.debug("Leaving check_api_key")


def query_by_title(
    api_url,
    api_key,
    movie_title,
    year=None,
    data_type=config.TYPE,
    plot=config.PLOT,
    result_type=config.RESULT_TYPE,
    version=config.VERSION,
    timeout=config.TIMEOUT,
):
    """Queries api_url using api_key for movie_title with additional api parameters."""
    logging.debug("Entering query_by_title")
    params = {
        "apikey": api_key,
        "t": movie_title,
        "i": None,
        "y": year,
        "type": data_type,
        "plot": plot,
        "r": result_type,
        "v": version,
    }
    params_without_nones = {k: v for k, v in params.items() if v is not None}
    result = requests.get(api_url, params=params_without_nones, timeout=timeout)
    logging.debug(f"Result: {result.text}")
    if result.status_code == 200:
        return result.json()
    else:
        raise Exception(f"Error when connecting to API: {result.text}")
    logging.debug("Leaving query_by_title")
