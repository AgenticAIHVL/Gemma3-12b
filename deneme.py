import asyncio
from browser_use import Agent
import ollama

async def simple_test():
    client = ollama.Client(host="http://157.157.221.29:19687")
    
    agent = Agent(
        task="Wait for the page to load and describe what you see",
        llm=client,
        browser_config={
            "headless": False,
            "viewport": {"width": 1920, "height": 1080},
            "slow_mo": 2000  # 2 saniye yavaş hareket
        },
        max_steps=5
    )
    
    # Browser'ı başlat ve direkt YouTube'a git
    await agent.browser.start()
    await agent.browser.page.goto("https://youtube.com")
    await agent.browser.page.wait_for_load_state('networkidle')
    
    # Şimdi agent'ı çalıştır
    result = await agent.run()
    print(result)

asyncio.run(simple_test())