import asyncio
from conva_ai.client import AsyncConvaAI 

def greeting():
    print("Ah, the ever-so-wise Boomers, \nthe perpetually self-aware Millennials, and \nthe remarkably knowledgeable Gen Z - together, we form the circle of eternal enlightenment!\n Welcome, wise sages of all ages, to another day of unrivaled wisdom and unending insight in the AI-powered wonderland! \nWhere machines dream of electric sheep and chatbots tell jokes!\n")
    print("Today I am going to do something mundane like answer your questions regarding Udemy! Dont go light on me. Go for it")
    
async def generate(client, query: str, stream: bool):
    response = client.invoke_capability(query, stream=stream)
    out = "" 
    async for res in response:
        out = res
    return out

async def main():
    client = AsyncConvaAI(
        copilot_id="cf4365f242294623a6b4ff2e6fb2bbaf", 
        api_key="663c4356752b4eb1b5a1486b6fa16a37", 
        copilot_version="1.0.0"
    )
    greeting()
    query = input("Your first question? (Type 'exit' to quit) ")
    while True:
        if query.lower() == "exit":
            break
        
        final_response = await generate(client, query, True)
        print(final_response.message + "\n")
        query = input("Next one? (Type 'exit' to quit) ")

if __name__ == "__main__":
    asyncio.run(main())
