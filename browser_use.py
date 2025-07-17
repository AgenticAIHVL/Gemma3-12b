import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from browser_use.llm import ChatOllama

# Ollama host'u environment variable olarak ayarla
os.environ['OLLAMA_HOST'] = 'http://157.157.221.29:19760'

async def main():
    agent = Agent(
        task="Open YouTube and search Browser-use videos and open third video",
        llm=ChatOllama(model="gemma3:12b")
    )
    await agent.run()

asyncio.run(main())