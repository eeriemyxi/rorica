# Rorica

> [!IMPORTANT]
> Rorica is still in development and currently **is unusable**.

Rorica is WebSocket-based chat server, also featuring an official React-based
static web client.

## Running Rorica
Copy `.env.sh.sample` to `.env.sh`. Also customize `LOG_LEVEL` between `debug`
and `info`.

> [!NOTE]
> The container does not depend on `.env.sh` file. That script just
> defines a bunch of environment variables for you.

Rorica leverages Docker containers.

**To run it for production**:

Set `RORICA_TARGET` to `production` in `.env.sh`.

```shell
source .env.sh
docker compose up
```

**To run it for development**:

Set `RORICA_TARGET` to `development` in `.env.sh`.

```shell
source .env.sh
docker compose up --watch
```
