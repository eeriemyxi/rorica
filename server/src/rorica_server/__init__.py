import websockets
import time
import asyncpg
import kisesi

kisesi.basic_config(level=kisesi.DEBUG)
log = kisesi.get_logger(__name__)

def main():
    log.info("Server is starting...")
