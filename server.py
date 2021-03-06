#!/usr/bin/env python3
"""
This code allows you to serve static files from the same port as the websocket connection
This is only suitable for small files and as a development server!
open(full_path, 'rb').read() call that is used to send files will block the whole asyncio loop!
"""

import os
import asyncio
import datetime
import random
import functools
import websockets
from http import HTTPStatus
import webbrowser

MIME_TYPES = {
    "html": "text/html",
    "js": "text/javascript",
    "css": "text/css"
}


async def process_request(sever_root, path, request_headers):
    print(dict(request_headers))
    print("ok")
    """Serves a file when doing a GET request with a valid path."""

    if "Upgrade" in request_headers:
        return  # Probably a WebSocket connection
    if path == '/':
        path += './index.html'

    response_headers = [
        ('Server', 'asyncio websocket server'),
        ('Connection', 'close'),
    ]

    # Derive full system path
    full_path = os.path.realpath(os.path.join(sever_root, path[1:]))

    # Validate the path
    if os.path.commonpath((sever_root, full_path)) != sever_root or \
            not os.path.exists(full_path) or not os.path.isfile(full_path):
        print("HTTP GET {} 404 NOT FOUND".format(path))
        return HTTPStatus.NOT_FOUND, [], b'404 NOT FOUND'

    extension = full_path.split(".")[-1]
    mime_type = MIME_TYPES.get(extension, "application/octet-stream")
    response_headers.append(('Content-Type', mime_type))

    # Read the whole file into memory and send it out
    body = open(full_path, 'rb').read()
    response_headers.append(('Content-Length', str(len(body))))
    print("HTTP GET {} 200 OK".format(path))
    return HTTPStatus.OK, response_headers, body


async def time(websocket, path):
    print("New WebSocket connection from", websocket.remote_address)
    while websocket.open:
        now = datetime.datetime.utcnow().isoformat()
        await websocket.send(now)

    print("WebSocket connection closed for", websocket.remote_address)


if __name__ == "__main__":

    handler = functools.partial(process_request, os.getcwd())
    start_server = websockets.serve(time, '0.0.0.0', 8000,
                                    process_request=handler)
    print(start_server)
    print("Running server at http://127.0.0.1:8000/")
    webbrowser.open_new_tab('http://127.0.0.1:8000/')
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()