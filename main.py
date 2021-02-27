import discord
import os
import random

client = discord.Client()
token = os.environ["BOT_TOKEN"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('ar.hello'):
        await message.channel.send('Hello!')

client.run(token)
