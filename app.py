import chainlit as cl
import ollama
import asyncio
import random

MODEL_NAME = "llama3.2-vision:latest"

greetings = [
    f"👋 Hi there! I’m your local AI assistant powered by **{MODEL_NAME}**. I run completely on your machine, so our conversations are private and secure. What’s on your mind today?",
    
    f"🤖 Hello! I’m your personal AI companion running on **{MODEL_NAME}**. Think of me as your co-pilot for learning, problem-solving, and exploring ideas — all while keeping your data safe locally. How can I assist you?",
    
    f"✨ Hey! I’m your AI sidekick, powered locally by **{MODEL_NAME}**. Whether you need help coding, writing, or just brainstorming creative ideas, I’m here to jump in. What should we dive into first?",
    
    f"⚡ Welcome aboard! I’m your AI assistant running fully on **{MODEL_NAME}**. My goal is to make your tasks easier, spark new ideas, and give you reliable answers — all without leaving your computer. How would you like to start?",
    
    f"🌱 Greetings! I’m your AI partner, operating on **{MODEL_NAME}** right here on your system. Together, we can explore knowledge, tackle challenges, or even just have a friendly conversation. What would you like to explore today?"
]

# ✅ Initialize session memory once when chat starts
@cl.on_chat_start
async def start_chat():
    cl.user_session.set(
        "interaction",
        [
            {
                "role": "system",
                "content": "You are a helpful assistant that maintains full context of the conversation.",
            }
        ],
    )

    msg = cl.Message(content="")
    start_message = random.choice(greetings)

    # stream greeting token by token
    for token in start_message:
        await msg.stream_token(token)

    await msg.send()

# ✅ Tool step (runs ollama while keeping session memory updated)
@cl.step(type="tool")
async def tool(input_message, image=None):
    interaction = cl.user_session.get("interaction")

    # store user message
    if image:
        interaction.append({"role": "user", "content": input_message, "images": image})
    else:
        interaction.append({"role": "user", "content": input_message})

    # run model in background thread
    response = await asyncio.to_thread(
        ollama.chat,
        model=MODEL_NAME,
        messages=interaction,   # ✅ pass full history
    )

    assistant_reply = response["message"]["content"]

    # store assistant reply in conversation history
    interaction.append({"role": "assistant", "content": assistant_reply})

    # update session so context persists
    cl.user_session.set("interaction", interaction)

    return assistant_reply

# ✅ Handles messages from user and maintains context
@cl.on_message
async def main(message: cl.Message):
    images = []
    if message.elements:
        images = [file for file in message.elements if hasattr(file, "mime") and "image" in file.mime]

    if images:
        tool_res = await tool(message.content, [i.path for i in images])
    else:
        tool_res = await tool(message.content)

    msg = cl.Message(content="")
    for token in tool_res:
        await msg.stream_token(token)

    await msg.send()
