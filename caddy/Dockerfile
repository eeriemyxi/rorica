FROM caddy:2.9-alpine AS base
WORKDIR /caddy
COPY . /caddy

FROM base AS development
CMD caddy run -c develop.caddyfile

FROM base AS production
CMD caddy run -c production.caddyfile
