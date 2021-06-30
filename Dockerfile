FROM python:3.9.6-alpine3.14
LABEL version="0.1"
LABEL maintainer="work@pawelwysokinski.pl"

RUN adduser -D app_user -h /app
USER app_user

ADD setup.py LICENSE README.md /app/
ADD movie_query /app/movie_query/
RUN cd /app && pip install .

WORKDIR ["/app"]
ENTRYPOINT ["/app/.local/bin/movie_query"]
