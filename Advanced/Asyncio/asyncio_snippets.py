"""
>>> import asyncio
>>> # You can use create_task() to schedule the execution of a coroutine object, followed by asyncio.run():
>>> async def coro(seq) -> list:
...     """'IO' wait time is proportional to the max element."""
...     await asyncio.sleep(max(seq))
...     return list(reversed(seq))
...
>>> async def main():
...     # This is a bit redundant in the case of one task
...     # We could use `await coro([3, 2, 1])` on its own
...     t = asyncio.create_task(coro([3, 2, 1]))  # Python 3.7+
...     await t
...     print(f't: type {type(t)}')
...     print(f't done: {t.done()}')
...
>>> t = asyncio.run(main())
t: type <class '_asyncio.Task'>
t done: True
>>> '''
There’s a subtlety to this pattern: if you don’t await t within main(), 
it may finish before main() itself signals that it is complete.

Because asyncio.run(main()) calls loop.run_until_complete(main()), 
the event loop is only concerned (without await t present) that main() is done, 
not that the tasks that get created within main() are done. 

Without await t, the loop’s other tasks will be cancelled, possibly before 
they are completed. 

If you need to get a list of currently pending tasks, you can use asyncio.Task.all_tasks().
'''
"""
"""
>>> # Notice how:
>>> async for i in range(100): pass # Doesn't work
>>> # Potential Fix 1:
>>> async def arange(count):
...     for i in range(count):
...         yield(i)
...
>>> # Or, a more in-depth fix:
>>> async def myrange(start, stop=None, step=1):
...     if stop:
            range_ = range(start, stop, step)
        else:
            range_ = range(start)
        for i in range_:
            yield i
            await asyncio.sleep(0)
>>>
