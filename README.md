# Rorica

> [!IMPORTANT]
> Rorica is still in development and currently is **unusable**.

Rorica is WebSocket-based chat server, also featuring a React-based official
static web client.

## Running Rorica
Rorica leverages Docker containers. To run it in production, do:

```shell
export RORICA_TARGET=production
docker compose up
```

To run the development version:
```shell
export RORICA_TARGET=develop
docker compose up --watch
```
