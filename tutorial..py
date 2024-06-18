import os
from openai import OpenAI
from apikey import apikey
import chainlit as cl
from openai import AsyncOpenAI

os.environ["OPENAI_API_KEY"] = apikey
client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}


@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )


@cl.on_message
async def main(message: cl.Message):
    client = OpenAI()
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message.content})
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "your an helpful assistant that helps student to understand concept in a way even 8th graders will",
            },
            {
                "role": "user",
                "content": message.content,
            },
        ],
        model="gpt-3.5-turbo",
        temperature=0.7,
    )

    content = response.choices[0].message.content
    msg = cl.Message(content)
    await msg.send()

    stream = client.chat.completions.create(
        messages=message_history, stream=True, **settings
    )

    async for part in stream:
        part = await part
        if token := part.choices[0].delta.content or "":
                await msg.stream_token(token)


    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()
