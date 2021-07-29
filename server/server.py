import logging
import platform
from asyncio.proactor_events import _ProactorBasePipeTransport
from functools import wraps

import aiohttp_cors
from aiohttp import log, web

from cloudpilot_token import TOKEN_TTL, generateToken, validateToken
from connection import Connection
from logger import logger

VERSION = 1

def start(host, port, ssl, logLevel, logLevelFramework, trustedOrigins, forceBindAddress = None):
    routes = web.RouteTableDef()

    async def handshakeHandler(request: web.Request):
        logger.info(f"issued token, lifetime {TOKEN_TTL} seconds")
        return web.json_response({'version': VERSION, 'token': generateToken()})

    @routes.get("/network-proxy/connect")
    async def connectHandler(request: web.Request):
        if not ("token" in request.query and validateToken(request.query["token"])):
            return web.Response(status = 403, text="403: forbidden")

        ws = web.WebSocketResponse()
        await ws.prepare(request)

        connection = Connection(forceBindAddress)
        await connection.handle(ws)

    _setupLogging(logLevel, logLevelFramework)

    app = web.Application()
    cors = aiohttp_cors.setup(app)

    resourceHandshake = cors.add(app.router.add_resource("/network-proxy/handshake"))
    cors.add(resourceHandshake.add_route("POST", handshakeHandler), {
        origin.strip(): aiohttp_cors.ResourceOptions(
            allow_headers=("Authorization",)
        ) for origin in trustedOrigins.split(",")
    })

    app.add_routes(routes)

    web.run_app(app, host=host, port=port, ssl_context=ssl)


def _setupLogging(logLevel, logLevelFramework):
    logging.basicConfig(level=logging.ERROR)

    for aiohttpLogger in (log.access_logger, log.server_logger):
        aiohttpLogger.setLevel(logLevelFramework.upper())

    logger.setLevel(logLevel.upper())

# Work around https://github.com/aio-libs/aiohttp/issues/4324

def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper

if platform.system() == 'Windows':
    _ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)
