FROM python:3.12-alpine AS base

ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

RUN apk add uv
RUN adduser -Ds /bin/sh rorica rorica

COPY --chown=rorica:rorica . /server
COPY . /server

WORKDIR /server

RUN uv sync

FROM base AS production
USER rorica
CMD uv run rorica-server --host 0.0.0.0 --port 80

FROM base AS development
RUN apk add entr findutils
USER rorica
CMD find src pyproject.toml | entr -rn uv run rorica-server --host 0.0.0.0 --port 80
