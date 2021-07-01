"""Main loop module."""

import logging
import os
import sys

import click
import validators

from . import api
from . import config
from . import exceptions


def setup_logging(debug):
    """Setup logging"""
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)


def validate_url(ctx, param, value): # pylint: disable=unused-argument
    """Used to check if api_url is indeed a url."""
    try:
        if validators.url(value) is True:
            return value
        else:
            raise click.BadParameter(f"{value} is not a valid url.")
    except Exception:
        raise click.BadParameter(f"Cannot parse api url: {value}.")


@click.command()
@click.option(
    "--debug", is_flag=True, default=False, show_default=True, help="Debug mode."
)
@click.option(
    "--api_url",
    callback=validate_url,
    type=click.UNPROCESSED,
    default=config.API_URL,
    show_default=True,
    help="Url of the open movie database.",
)
@click.option(
    "--api_key",
    type=str,
    help="Open movie database api key (can also be provided via env variable MOVIE_QUERY_API_KEY).",
)
@click.option(
    "--rating_source",
    type=str,
    show_default=True,
    default=config.RATING_SOURCE,
    help="Rating source to fetch rating for.",
)
@click.argument("movie_title", type=str)
def main(debug, api_url, api_key, rating_source, movie_title):
    """
    This tool returns a rating from RATING_SOURCE for MOVIE_TITLE from Open Movie database API_URL.
    """
    try:
        setup_logging(debug)
        api_key = (
            os.environ.get("MOVIE_QUERY_API_KEY", "") if api_key is None else api_key
        )
        api.check_api_key(api_url, api_key)
        print(get_movie_rating(api_url, api_key, movie_title, rating_source))
        sys.exit(0)
    except exceptions.MovieNotFoundException:
        logging.error(f"Movie {movie_title} not found!")
        sys.exit(1)
    except Exception:
        logging.exception("Something went wrong during execution.")
        logging.error("Exception was thrown. Exiting.")
        sys.exit(2)


def get_movie_rating(api_url, api_key, movie_title, source):
    """
    Returns a rating for a specific source for a movie_title.
    N/A is returned if rating not found.
    """
    logging.debug("Entering get_movie_ratings")
    result = api.query_by_title(api_url, api_key, movie_title)
    if isinstance(result, dict):
        if "Error" in result and result["Error"] == "Movie not found!":
            raise exceptions.MovieNotFoundException()
        elif "Error" in result:
            raise Exception("Error in getting movie.")
        else:
            if "Ratings" in result:
                return get_rating_for_source(result["Ratings"], source)
            else:
                return "N/A"
    else:
        raise TypeError("Expected a dict as a result from DB query.")
    logging.debug("Leaving get_movie_ratings")


def get_rating_for_source(list_of_ratings, source):
    """Helper function for getting the rating from list of sources"""
    for rating in list_of_ratings:
        if rating["Source"] == source:
            return rating["Value"]
    return "N/A"


if __name__ == "__main__":
    main() # pylint: disable=no-value-for-parameter
