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
    
    # Interaction-talking commands
    
    if message.content.startswith('ar.hi'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('ar.hello'):
        await message.channel.send('Hi!')
        
    if message.content.startswith('ar.ask'):
        if message.content[7:] == 'How are you?':
            answer = [ "Really good!"
                     , "I am bored -_-"
                     , "Cool!"
                     , "Not now."
                     , "Pogs and Champs, Feeling good right now!"
                     ]
            await message.channel.send(random.choice(answer))
            

client.run(token)
