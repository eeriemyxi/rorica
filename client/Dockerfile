FROM oven/bun:1.1.42-alpine AS base

# RUN useradd -ms /bin/sh -u 1001 rorica
RUN adduser -Ds /bin/sh rorica rorica

USER rorica
WORKDIR /client

COPY --chown=rorica:rorica . /client
RUN bun install

FROM base AS production
RUN bun run build
RUN touch /client/ready
CMD tail -f /dev/null

FROM base AS development
CMD bun run dev --port 80 --host 0.0.0.0
