# Incomplete Example
```
"""
Authored By: Lynn Root at https://www.roguelynn.com/words/asyncio-we-did-it-wrong-pt-1/
Additional Reading: https://asyncio.readthedocs.io/en/latest/producer_consumer.html
GitHub source for Example: https://github.com/econchick/mayhem

Lynn says: This is an event-driven service that consumes from a
  pub/sub, and initiates a mock restart of a host. 
  We could get thousands of messages in seconds, so as we get a message,
  we shouldn’t block the handling of the next message we receive.
"""
'''
Notice! This requires: 
 - attrs==18.1.0
'''

import asyncio
import logging
import random
import string

import attr


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s,%(msecs)d %(levelname)s: %(message)s',
    datefmt='%H:%M:%S',
)


@attr.s
class PubSubMessage:
    instance_name = attr.ib()
    message_id    = attr.ib(repr=False)
    hostname      = attr.ib(repr=False, init=False)

    def __attrs_post_init__(self):
        self.hostname = f'{self.instance_name}.example.net'


# simulating an external publisher of events
async def publish(queue, n):
    choices = string.ascii_lowercase + string.digits

    for x in range(1, n + 1):
        host_id = ''.join(random.choices(choices, k=4))
        instance_name = f'cattle-{host_id}'
        msg = PubSubMessage(message_id=x, instance_name=f'cattle-{host_id}')
        await queue.put(msg)
        logging.info(f'Published {x} of {n} messages')

    await queue.put(None)  # publisher is done


async def consume(queue):
    while True:
        # wait for an item from the publisher
        msg = await queue.get()
        if msg is None:  # publisher is done
            break

        # process the msg
        logging.info(f'Consumed {msg}')
        # unhelpful simulation of i/o work
        await asyncio.sleep(random.random())


if __name__ == '__main__':
    queue = asyncio.Queue()
    publisher_coro = publish(queue, 5)
    consumer_coro = consume(queue)
    asyncio.run(publisher_coro)
    asyncio.run(consumer_coro)
```
