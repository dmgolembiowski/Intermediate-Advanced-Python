from __future__ import annotations
import typing
""" Intermediate/Asyncio/errorHandling.py 

An example for wrapping coroutines that catch
unexpected Exceptions during the course of the
event.

Hugely inspired by Lynn Root's tutorial, "Mayhem Mandrill"
"""

import asyncio
import string
import random
import logging

async def publish(queue: asyncio.Queue, n: typing.int):
    # do things 
    # ...
    await queue.put(None)


async def consume(queue: asyncio.Queue):
    # do things
    # ...
    while True:
        msg = queue.get()
        if msg is None:
            break

# This is the WRAPPER part that matters:
async def handle_exception(coro, loop):
    try:
        await coro
    except Exception as e:
        logging.error(f"Caught exception: {e}")
        loop.stop()

if __name__ == '__main__':
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()

    # See the `handle_exception` usage
    publisher = handle_exception(
            publish(queue, 5),
            loop)

    # Again, see here
    consumer = handle_exception(
            consume(queue),
            loop)

    loop.create_task(publisher)
    loop.create_task(consumer)
    try:
        loop.run_forever()
    finally:
        logging.info('Cleaning up')
        loop.close()

