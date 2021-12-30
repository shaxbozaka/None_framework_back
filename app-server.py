#!/usr/bin/env python
import sys

print("server 2 has started own work!!")

import asyncio, os
import dashboard
from urllib.parse import urlparse, parse_qs



async def handle_client(reader, writer):
    type_data = "HTTP/1.1 200 ok\r\n" \
                "Content-type: text/html\r\n\r\n".encode('utf-8')
    data = (await reader.read(4096)).decode()
    method = str(data.split()[0])
    print(sys.argv)
    if method.upper() == "GET":
        parsedurl = parse_qs(urlparse(data).query)
        if sys.argv[1]:
            writer.write(type_data + b'docker')
        if dashboard.write(parsedurl, True):
            writer.write(type_data + b'ok <a href=\'/\'>home</a>')
        else:
            writer.write(type_data + b'we have somewhere error <a href=\'/\'>home</a>')
    else:
        writer.write(type_data + b"method not found! <a href=\'/\'>home</a>")
    writer.close()


loop = asyncio.get_event_loop()
loop.create_task(asyncio.start_server(handle_client, '0.0.0.0', 8080))
loop.run_forever()
