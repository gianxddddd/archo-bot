import asyncio
import discord
import os
import random
import youtube_dl

client = discord.Client()
token = os.environ["BOT_TOKEN"]
queue = {}

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='ar.help'))
    print('Logged in {0.user}'.format(client))
  
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # General bot commands
    
    if message.content.startswith('ar.welcome'):
        embed = discord.Embed(title="Archo", description="Hi, I am Archo! Type `ar.help` for more commands.", color=0x03a9f4)
        embed.add_field(name="Join our Discord server:", value="https://discord.gg/x5t9n9fWCV", inline=False)
        embed.add_field(name="Follow the developer on Twitter:", value="https://twitter.com/GianXDDDDD", inline=False)
        embed.set_footer(text=f"Command issued by {message.author} - Archo")
        await message.channel.send(embed = embed)
        
    if message.content.startswith('ar.invite') or message.content.startswith('ar.invites'):
        embed = discord.Embed(title="Invite Links", color=0x03a9f4)
        embed.add_field(name=":robot: Bot Invitation:", value="https://bit.ly/2MUkD3i", inline=False)
        embed.add_field(name="<:archo_bot:817292777673981982> Discord server invitation:", value="https://bit.ly/2OydndU", inline=False)
        embed.set_footer(text=f"Command issued by {message.author} - Archo")
        await message.channel.send(embed = embed)

    if message.content.startswith('ar.help'):
        embed = discord.Embed(title="Help", description="Here are the commands you can interact with Archo:", color=0x03a9f4)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805357950221942794/816279533920714752/20210227_221617.png")
        embed.add_field(name=":speech_balloon: General", value="`ar.welcome, ar.help, ar.invite, ar.status, ar.about`", inline=False)
        embed.add_field(name=":musical_note: Music", value="`ar.play <url>, ar.download <url>, ar.pause, ar.resume, ar.stop, ar.connect, ar.disconnect`", inline=False)
        embed.add_field(name=":rofl: Fun", value="`ar.codefacts, ar.secretmsg <message>, ar.die, ar.megadie ar.supermegadie, ar.supermegabunchdoperhuntadie, ar.pog, ar.hoomancheck`", inline=False)
        embed.add_field(name="<:sus:807092771806248990> Misc", value="`ar.music.app`", inline=False)
        embed.set_footer(text=f"Command Issued by {message.author} - Archo")
        await message.channel.send(embed = embed)
        
    if message.content.startswith('ar.status') or message.content.startswith('ar.stats'):
        statuses = [ "Online"
                   , "AAAA!"
                   , "Listening to a Chinese song."
                   , "Watching Netflix with my bot girlfriend."
                   , "Playing Minecraft."
                   , "Are ya winning son?"
                   , "gianxddddd.aternos.me :sus:"
                   ]
        embed = discord.Embed(title="Bot Status", color=0x03a9f4)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805357950221942794/816279533920714752/20210227_221617.png")
        embed.add_field(name=":green_circle: Active Status", value=random.choice(statuses), inline=False)
        embed.add_field(name=":signal_strength: Latency", value=f"{str(round((client.latency) * 1000))} ms", inline=False)
        embed.add_field(name=":flag_white: Joined Servers", value=f"{str(len(client.guilds))} servers", inline=False)
        embed.add_field(name=":robot: Bot Prefix", value="`ar.<command>`", inline=False)
        embed.set_footer(text=f"Command issued by {message.author} - Archo")
        await message.channel.send(embed = embed)
        
    if message.content.startswith('ar.about') or message.content.startswith('ar.info') or message.content.startswith('ar.information'):
        embed = discord.Embed(title="About & Information", description="Archo is a Discord bot rewritten and based on Archo Music discord bot.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/805357950221942794/816279533920714752/20210227_221617.png")
        embed.add_field(name=":information_source: Version", value="v7.18py", inline=False)
        embed.add_field(name=":technologist: Creator", value="GianXD", inline=False)
        embed.add_field(name=":broom: Maintainer", value="Pranav", inline=False)
        embed.set_footer(text=f"Command issued by {message.author} - Archo")
        await message.channel.send(embed = embed)

    # Music Commands
     
    if message.content.startswith('ar.connect') or message.content.startswith('ar.join'):
        if message.author.voice is None:
             embed = discord.Embed(color=0x03a9f4)
             embed.add_field(name="Error", value="You are not in a voice channel.", inline=True)
             await message.channel.send(embed = embed)
        else:
             try:
                 if discord.voice.is_connected():
                    await message.guild.voice_client.move_to(message.author.voice.channel)
                    embed2 = discord.Embed(color=0x03a9f4)
                    embed2.add_field(name="Archo", value=F"Joined {message.author.voice.channel} voice channel.", inline=True)
                    await message.channel.send(embed = embed2)
             except AttributeError:
                discord.voice = await message.author.voice.channel.connect()
                embed3 = discord.Embed(color=0x03a9f4)
                embed3.add_field(name="Archo", value=F"Joined `{message.author.voice.channel}` voice channel.", inline=True)
                await message.channel.send(embed = embed3)

    if message.content.startswith('ar.disconnect') or message.content.startswith('ar.dc') or message.content.startswith('ar.leave'):
        try:
            if discord.voice.is_connected():
                if message.author.voice.channel is None:
                    embed = discord.Embed(color=0x03a9f4)
                    embed.add_field(name="Error", value="You are not in a voice channel.", inline=True)
                    await message.channel.send(embed = embed)
                else:
                    await discord.voice.disconnect()
                    discord.voice = None
                    embed2 = discord.Embed(color=0x03a9f4)
                    embed2.add_field(name="Archo Music", value=F"Left `{message.author.voice.channel}` voice channel.", inline=True)
                    await message.channel.send(embed = embed2)
            else:
                 embed3 = discord.Embed(color=0x03a9f4)
                 embed3.add_field(name="Error", value="The bot is not in the voice channel you are currently in.", inline=True)
                 await message.channel.send(embed = embed3)
        except AttributeError:
            embed4 = discord.Embed(color=0x03a9f4)
            embed4.add_field(name="Error", value="You are not in a voice channel.", inline=True)
            await message.channel.send(embed = embed4)

    if message.content.startswith('ar.play'):
        if message.author.voice != None:
            try:
                if discord.voice.is_connected():
                    await message.guild.voice_client.move_to(message.author.voice.channel)
            except AttributeError:
                discord.voice = await message.author.voice.channel.connect()
            if discord.voice.is_playing():
                discord.voice.stop()
                if message.content[8:].startswith('http://www.youtube.com') or message.content[8:].startswith('https://www.youtube.com') or message.content[8:].startswith('http://youtu.be') or message.content[8:].startswith('https://youtu.be') or message.content[8:].startswith('http://m.youtube.com') or message.content[8:].startswith('https://www.m.youtube.com'):
                    if message.content[8:].endswith('start_radio=1'):
                        embed2 = discord.Embed(color=0x03a9f4)
                        embed2.add_field(name="Error", value="Cannot retrieve a playlist.", inline=True)
                        await message.channel.send(embed = embed2)
                    else:
                        global queue
                        try:
                            queue[message.guild.id].append(message.content[8:])
                        except:
                            queue[message.guild.id] = [message.content[8:]]
                        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 0', 'options': '-vn'}
                        ydl_opts = {'format': 'bestaudio'}
                        with youtube_dl.YoutubeDL(ydl_opts) as ytdl:
                            info = ytdl.extract_info(queue[message.guild.id][0], download=False)
                            URL = info['formats'][0]['url']
                        discord.voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                        await message.delete()
                        del(queue[message.guild.id][0])
                        embed3 = discord.Embed(title="Now Playing", description=info['title'], url=message.content[8:], color=0x03a9f4)
                        embed3.set_thumbnail(url=info['thumbnail'])
                        embed3.set_footer(text=f"Requested by {message.author} - Archo")
                        await message.channel.send(embed = embed3)
                else:
                    embed4 = discord.Embed(color=0x03a9f4)
                    embed4.add_field(name="Error", value="Cannot retrieve YouTube video. <:doggo_cheems:737772621751517345>", inline=True)
                    await message.channel.send(embed = embed4)
        else:
            embed5 = discord.Embed(color=0x03a9f4)
            embed5.add_field(name="Error", value="You are not in a voice channel.", inline=True)
            await message.channel.send(embed = embed5)

    if message.content.startswith('ar.resume'):
        if discord.voice.is_connected():
            if discord.voice.is_paused():
                discord.voice.resume()
                embed = discord.Embed(color=0x03a9f4)
                embed.add_field(name="Now Playing", value="Playback has been resumed.", inline=True)
                await message.channel.send(embed = embed)
        else:
            embed2 = discord.Embed(color=0x03a9f4)
            embed2.add_field(name="Error", value="The bot is not in the voice channel you are currently in.", inline=True)
            await message.channel.send(embed = embed2)

    if message.content.startswith('ar.pause'):
        if discord.voice.is_connected():
            if discord.voice.is_playing():
                discord.voice.pause()
                embed = discord.Embed(color=0x03a9f4)
                embed.add_field(name="Now Playing", value="Playback has been stopped.", inline=True)
                await message.channel.send(embed = embed)
        else:
            embed2 = discord.Embed(color=0x03a9f4)
            embed2.add_field(name="Error", value="The bot is not in the voice channel you are currently in.", inline=True)
            await message.channel.send(embed = embed2)

    if message.content.startswith('ar.stop'):
        if discord.voice.is_connected():
            if discord.voice.is_paused() or discord.voice.is_playing():
                discord.voice.stop()
            
    if message.content.startswith('ar.download'):
        embed = discord.Embed(color=0x03a9f4)
        embed.add_field(name="Error", value="Command unavailable. <:doggo_cheems:737772621751517345>", inline=False)
        await message.channel.send(embed = embed)
        
    # Fun Commands
    
    if message.content.startswith('ar.die'):
        await message.channel.send('NO U')
        
    if message.content.startswith('ar.megadie'):
        await message.channel.send('no.')
        
    if message.content.startswith('ar.supermegadie'):
        await message.channel.send('Go to hell.')
        
    if message.content.startswith('ar.secretmsg'):
        if message.content.startswith('ar.secretmsg'):
            await message.channel.send(message.content[13:])
        else:
            if message.content.startswith('ar.secretmessage'):
                await message.channel.send(message.content[16:])
        await message.delete()

    if message.content.startswith('ar.codefacts') or message.content.startswith('ar.codefact') or message.content.startswith('ar.codingfacts') or message.content.startswith('ar.codingfact'):
        codingfacts = [ "Coders might get stuck in an error for 2 hours just to add semicolons."
                      , "67% of all programming jobs are in industries outside of technology."
                      , "You can't create a video game without programming."
                      , "Most students like programming."
                      , "The easiest programming language to learn is Python."
                      , "IDEs can cause high memory usage, reduce it by using the manuals."
                      , "Sketchware is a code-block android application which creates a real Android application."
                      , "Learning Math also improves your programming knowledge."
                      , "Java/XML/Kotlin/Groove/C++ are the only programming languages you can create an Android application with."
                      , "Linux is preferred as the programming-like Operating System and is 25% faster than Windows."
                      , "There are over 700 different programming languages!"
                      , "Python is one of the most popular programming language."
                      , "Smart enough, you can compile your project using a Terminal or a Console."
                      , "Android Studio is the most preferred IDE for beginners."
                      ]
        embed = discord.Embed(color=0x03a9f4)
        embed.add_field(name="Coding Facts", value=random.choice(codingfacts), inline=False)
        await message.channel.send(embed = embed)
    
    if message.content.startswith('ar.hoomancheck'):
        await message.channel.send('Identifying user...')
        await asyncio.sleep(0.100)
        identification = [ "Pog! You're a hooman!"
                    , "Ehh? Failed to identify user."
                    , "Holy sh#!t, you're a cow."
                    , "Wow, didn't know you're a monkey!"
                    , "Meow, You're a cat."
                    , "Uhhh... You are a leaf."
                    , "I am tired, make a request to identify later."
                    , "☌⍀⟒⟒⏁⟟⋏☌⌇ ⎎⍀⍜⋔ ⟒⏃⍀⏁⊑, ⊬⍜⎍ ⏃⍀⟒ ⏃⋏ ⏃⌰⟟⟒⋏."
                    , "What the $#@! You're a ghost."
                    , "UnsatisfiedUser.com"
                    ]
        await message.channel.send(random.choice(identification))
        
    if message.content.startswith('ar.pog'):
        pogs = [ "Pogchamp!"
               , "Poggers!"
               , "Pog!"
               , "pog-aaugghhh"
               , "Champpog"
               , "Pog-Pog-Pog"
               , "Pogs-and-Champs!"
               ]
        await message.channel.send(random.choice(pogs))
        
    # Archo Apps Commands
    
    if message.content.startswith('ar.music.app'):
        embed = discord.Embed(title="Archo", color=0x03a9f4)
        embed.add_field(name="Download Archo Music from Sketchub:", value="https://project.sketchub.in/?id=403", inline=False)
        embed.add_field(name="or from Github:", value="https://github.com/gianxddddd/archo-music/releases/download/v5.17/Archo_Music.apk", inline=False)
        embed.set_footer(text=f"Command issued by {message.author} - Archo")
        await message.channel.send(embed = embed)
        
    # Misc Commands

    if message.content == 'ar.' or message.content == 'ar':
        embed = discord.Embed(color=0x03a9f4)
        embed.add_field(name="Error", value="Command not listed. Forgot the commands? Type `ar.help` to view all commands.", inline=True)
        await message.channel.send(embed = embed)

    if message.content.startswith('ar.pytools'):
       print('https://cog-creators.github.io/discord-embed-sandbox/')
    
    
client.run(token)
