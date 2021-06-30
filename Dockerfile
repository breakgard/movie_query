FROM python:3.9.6-alpine3.14
LABEL version="0.1"

ADD setup.py LICENSE README.md /app/
ADD movie_query /app/movie_query/
RUN cd /app && python3 setup.py install && rm -rf build dist movie_query.egg.info

ENTRYPOINT ["/usr/local/bin/movie_query"]
