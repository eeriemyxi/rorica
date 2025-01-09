import argparse
import asyncio
from functools import partial
from http import HTTPStatus

import asyncpg
import kisesi
from websockets.asyncio.server import serve

from . import const

kisesi.basic_config(level=const.LOG_LEVEL)
log = kisesi.get_logger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, required=True)
parser.add_argument("--port", type=int, required=True)


def handle_request(connection, request):
    if request.path == "/health":
        return connection.respond(HTTPStatus.OK, "OK\n")


async def base(websocket, con):
    async for message in websocket:
        await websocket.send(message)


async def start(host: str, port: int):
    con = await asyncpg.connect(
        host=const.PG_HOST,
        port=const.PG_PORT,
        user=const.PG_USER,
        password=const.PG_PASSWORD,
    )
    log.info(f"Server is starting on {host}:{port}")

    async with serve(
        partial(base, con), host, port, process_request=handle_request
    ) as server:
        await server.serve_forever()


def main():
    args = parser.parse_args()

    log.debug(f"{const.PG_HOST=}")
    log.debug(f"{const.PG_PORT=}")
    log.debug(f"{const.PG_USER=}")
    log.debug(f"{const.PG_PASSWORD=}")

    asyncio.run(start(args.host, args.port))
