FROM python:3.12-alpine AS base
RUN apk add uv

RUN adduser -Ds /bin/sh rorica rorica

USER rorica
WORKDIR /server

COPY --chown=rorica:rorica . /server
RUN uv sync

FROM base AS production
CMD uv run rorica-server

FROM base AS develop

USER root
RUN apk add entr findutils

USER rorica
CMD find src pyproject.toml | entr -nr uv run rorica-server
