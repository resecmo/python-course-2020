import asyncio
import json
import time

from concurrent.futures import FIRST_COMPLETED
from dataclasses import dataclass  # Starting from Python 3.7

import aiohttp


@dataclass
class Service:
    name: str
    url: str
    ip_attribute: str


SERVICES = (
    Service(
        name='ipify', url='https://api.ipify.org?format=json', ip_attribute='ip'
    ),
    Service(
        name='ip-api', url='http://ip-api.com/json', ip_attribute='query'
    ),
)


async def fetch_ip(service):
    async with aiohttp.ClientSession() as session:
        async with session.get(service.url) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()

            return service.name, json.loads(html)[service.ip_attribute]


async def asynchronous():
    coroutines = [asyncio.create_task(fetch_ip(SERVICES[i])) for i in range(2)]
    done, _ = await asyncio.wait(coroutines, return_when=FIRST_COMPLETED)
    print(done.pop().result())


loop = asyncio.get_event_loop()
loop.run_until_complete(asynchronous())