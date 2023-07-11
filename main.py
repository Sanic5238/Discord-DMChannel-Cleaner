import discord
from discord.ext import commands
import asyncio

with open('token.txt', 'r') as f:
    TOKEN = f.read().strip()

client = discord.Client()
channels = ['']

@client.event
async def on_ready():
    print('Ready')

async def main():
    print("Waiting Average Load Time")
    await asyncio.sleep(10)

    for i in range (1, 50):
        for x in client.private_channels:
            
            if str(x.id) in channels:
                print(F"Found DM With {x.recipient} Deleting now!")
                async for message in x.history(limit=10000):
                    if message.author == client.user:
                        print(F'Deleted a message')
                        try:
                            await message.delete()
                        except:
                            continue
                                
                        
                print('Finished Deletion, enjoy!')


client.loop.create_task(main())
try:
    print("Logging in...")
    client.run(TOKEN, bot=False)
except Exception as e:
    print(e)
