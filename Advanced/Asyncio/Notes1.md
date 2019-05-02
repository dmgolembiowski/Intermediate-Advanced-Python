# A more complete example
## Originally published at: https://faculty.ai/blog/a-guide-to-using-asyncio/
`Having coroutines yield control of the event loop is most helpful when it’s anticipated that we’re going to have to wait idle for a while until some useful work can be done. We can emulate this case with asyncio.sleep, which simply waits for a specified number of seconds before completing:`

```
import asyncio

async def print_after(message, delay):
    """Print a message after the specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(message)

async def main():
    # Use asyncio.gather to run two coroutines concurrently:
    await asyncio.gather(
        print_after("world!", 2),
        print_after("Hello", 1)
    )

asyncio.run(main())
```

# When do coroutines (async functions) start running?
`A common pitfall when using coroutines with asyncio is that they sometimes need to be scheduled on the event loop explicitly. `
`Asyncio doesn’t start the execution of a coroutine until one is explicitly registered with it (such as with asyncio.run()) or you await it in another coroutine. If we want to start multiple coroutines and have them run concurrently as above, we can either use asyncio.gather() as in the earlier example, or schedule them individually with asyncio.create_task():`

```
import asyncio

async def print_after(message, delay):
    """Print a message after the specified delay (in seconds)"""
    await asyncio.sleep(delay)
    print(message)

async def main():
    # Start coroutine twice (hopefully they start!)
    first_awaitable = asyncio.create_task(print_after("world!", 2))
    second_awaitable = asyncio.create_task(print_after("Hello", 1))
    # Wait for coroutines to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())
```

# Running Commands
import asyncio
```
async def echo(string):
    process = await asyncio.create_subprocess_exec("echo", string)
    await process.wait()

asyncio.run(echo("Hello, world!"))
"""
Processes are created using asyncio.create_subprocess_exec() 
(which is itself a coroutine and so needs to be awaited). 
Some of the methods on the process object are also 
coroutines (like .wait() in the above example).
"""
```
# Asynchronous HTTP with aiohttp
```
Our job agent is also responsible for sending information 
back to a central tracking server. For example, to 
determine the health of the job and allow the central 
service to take action when a job becomes unhealthy.

Making a network request is another I/O bound operation 
that fits well with a coroutine-based concurrency 
programming model. We used aiohttp, a popular HTTP library 
built on top of asyncio, to send monitoring information 
back to our tracking service.

To make an HTTP request with aiohttp:
```
```
import aiohttp
import asyncio

async def fetch_and_print(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        print(await response.text())

asyncio.run(fetch_and_print("https://python.org/"))
"""
The above example uses an aiohttp.ClientSession as an 
asynchronous context manager with the async wait syntax. 
This works much in the same way as standard context 
managers in Python, except that the code that governs 
entering and exiting the context is implemented in a 
coroutine and so can also be executed asyncronously. 
In this case, using the session as a context manager 
ensures that it is closed when we’re done with it.
"""
# See the complete example at https://github.com/acroz/asyncio-example
```
