FROM caddy:2.9-alpine AS base
WORKDIR /caddy
COPY . /caddy

FROM base AS develop
CMD caddy run -c develop.caddyfile

FROM base AS production
# [TODO] Find a way to get dist/ files from `client` container.
CMD ls
