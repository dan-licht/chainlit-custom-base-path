import time

import chainlit as cl


def sync_function():
    time.sleep(5)


@cl.on_chat_start
async def start():
    await cl.Message(content="Message 1").send()
    await cl.make_async(sync_function)()
    await cl.Message(content="Message 2").send()


@cl.on_message
async def message(message: cl.Message):
    await cl.Message(content="World").send()
