from . import api

import click
import logging
import os
import sys
import validators

def setup_logging(debug):
  if debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.ERROR)

def validate_url(ctx, param, value):
  try:
    if validators.url(value) == True:
      return value
    else:
      raise click.BadParameter(f"{value} is not a valid url.")
  except Exception:
    raise click.BadParameter(f"Cannot parse api url: {value}.")

@click.command()
@click.option("--debug", is_flag=True, default=False, show_default=True, help="Debug mode.")
@click.option("--api_url", callback=validate_url, type=click.UNPROCESSED, default="http://www.omdbapi.com", show_default=True, help="Url of the open movie database.")
@click.option("--api_key", type=str, help="Open movie database api key (can also be provided via env variable MOVIE_QUERY_API_KEY).")
@click.argument("movie_name", type=str)
def main(debug, api_url, api_key, movie_name):
  try:
    setup_logging(debug)
    api_key = os.environ.get("MOVIE_QUERY_API_KEY") if api_key is None else api_key
    api.check_api_key(api_url, api_key)
    print(get_movie_rating(api_url, api_key, movie_name))
    sys.exit(0)
  except Exception:
    logging.exception("Something went wrong during execution.")
    logging.error("Exception was thrown. Exiting.")
    sys.exit(2)

def get_movie_rating(api_url, api_key, movie_name, source='Rotten Tomatoes'):
  logging.debug("Entering get_movie_ratings")
  result = api.query_by_title(api_url, api_key, movie_name)
  if isinstance(result, dict):
    if "Error" in result:
      logging.error(f"Cannot get movie {movie_name}: {result}")
      sys.exit(1)
    else:
      if "Ratings" in result:
        return get_rating_for_source(result["Ratings"], source)
      else:
        return "N/A"
  else:
    raise TypeError("Expected a dict as a result from DB query.")
  logging.debug("Leaving get_movie_ratings")

def get_rating_for_source(list_of_ratings, source):
  for rating in list_of_ratings:
    if rating["Source"] == source:
      return rating["Value"]
  return "N/A"

if __name__ == "__main__":
  main()
