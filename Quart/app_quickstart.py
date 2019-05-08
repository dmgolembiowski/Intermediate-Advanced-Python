#!/usr/bin/env python3

from quart import Quart
import aiofiles

# Create an instance of the `Quart` application class
app = Quart(__name__)

# Use a coroutine to return HTML template
async def html_document(path: str) -> str:
    """ `html_document()` is a coroutine,
    so it should be awaited for execution"""
    async with aiofiles.open(path, mode='r') as f:
        page = await f.read()
    return page

@app.route('/')
async def render_page():
    return await html_document("index.html")

app.run()
