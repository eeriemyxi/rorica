# Rorica

> [!IMPORTANT]
> Rorica is still in development and currently **is unusable**.

Rorica is WebSocket-based chat server, also featuring an official React-based
static web client.

## Running Rorica
Rorica leverages Docker containers.

To run it for production:
```shell
export RORICA_TARGET=production
docker compose up
```

To run it for development:
```shell
export RORICA_TARGET=develop
docker compose up --watch
```
