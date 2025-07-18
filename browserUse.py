import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from browser_use.llm import ChatOllama

# Ollama host'u environment variable olarak ayarla
os.environ['OLLAMA_HOST'] = 'http://157.157.221.29:19687'

async def main():
    agent = Agent(
        task="Go to imbd's web site."
            "Show most popular movies.",
        
             
        llm=ChatOllama(model="llama3.1:8b"
        ))
    
    await agent.run()

asyncio.run(main())