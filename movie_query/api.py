import requests
import logging
from . import api_config

def check_api_key(api_url, api_key, timeout=api_config.TIMEOUT):
  logging.debug("Entering check_api_key")
  params = {
    "apikey": api_key
  }
  result = requests.get(api_url, params=params, timeout=timeout)
  logging.debug(f"Result: {result.text}")
  if result.status_code != 200:
    if result.status_code == 401:
      raise Exception("Api key is invalid or not provided.")
    else:
      raise Exception(f"Error when connecting to API: {result.text}")
  logging.debug("Leaving check_api_key")

def query_by_title(api_url, api_key, movie_title, y=None,
                    type=api_config.TYPE, plot=api_config.PLOT,
                    r=api_config.RESULT_TYPE, v=api_config.VERSION,
                    timeout=api_config.TIMEOUT):
  logging.debug("Entering query_by_title")
  params = {
    "apikey": api_key,
    "t": movie_title,
    "i": None,
    "y": y,
    "type": type,
    "plot": plot,
    "r": r,
    "v": v
  }
  params_without_nones = {k: v for k,v in params.items() if v is not None}
  result = requests.get(api_url, params=params_without_nones, timeout=timeout)
  logging.debug(f"Result: {result.text}")
  if result.status_code == 200:
    return result.json()
  else:
    raise Exception(f"Error when connecting to API: {result.text}")
  logging.debug("Leaving query_by_title")
