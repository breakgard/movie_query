# movie_query
A small CLI app to query an external API containing movie info.
Currently supported API is [Open movie database](https://www.omdbapi.com).

## General info

The current version of the code takes a name of a movie on input and fetches
a Rotten Tomatoes rating for a best fitting match.
Providing that the rating and the movie exist in the database.

## Requirements

1. You will need an activated Open Movie Database API key.
   You can generate one using an email address [here](https://www.omdbapi.com/apikey.aspx).
2. Docker is the recommended way of running this app.
   Instructions on how to install docker can be found [here](https://docs.docker.com/engine/install/).
3. To run without docker, the following versions of python are supported (might work on other 3.X):
    - 3.9.6

## Install

### Docker

To build the docker image locally, just run the following statement in the main working directory of the repo:
```
docker build . --tag movie_query:local
```

### Virtualenv

Another way of running this app is via a virtual env.
On Linux, run the following in the main working directory of the repo:
```
python3 -m venv venv
. venv/bin/activate
python3 -m pip install pip --upgrade
pip install .
```

## Usage

### Docker

Provided that the image was built how it was described in this readme,
you can run to view the current help message:
```
docker run movie_query:local --help
```

### Virtualenv

## Output

The code returns the rating value for the movie to stdout.
If the movies does not have a rating, it returns `N/A`.
In case of failure, it returns nothing on stdout (only stderr).

## Examples

Regular usage:
```
export MOVIE_QUERY_API_KEY=<YOUR_OMDB_API_KEY>
docker run -e MOVIE_QUERY_API_KEY=${MOVIE_QUERY_API_KEY} movie_query:local Test
```

Debug usage:
```
export MOVIE_QUERY_API_KEY=<YOUR_OMDB_API_KEY>
docker run -e MOVIE_QUERY_API_KEY=${MOVIE_QUERY_API_KEY} movie_query:local Test --debug
```

For virtual env, run the following in an activated environment:
```
export MOVIE_QUERY_API_KEY=<YOUR_OMDB_API_KEY>
movie_query Test
```

## Error codes

- 0 - OK
- 1 - Handled error (example: movie cannot be found)
- 2 - Unhandled exception
