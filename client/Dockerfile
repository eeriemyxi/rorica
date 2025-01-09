FROM oven/bun:1.1.42 AS base

RUN useradd -ms /bin/sh -u 1001 rorica

USER rorica
WORKDIR /client

COPY --chown=rorica:rorica . /client
RUN bun install

FROM base AS production
CMD bun run build

FROM base AS development
CMD bun run dev --port 80 --host 0.0.0.0
