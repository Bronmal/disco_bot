import sys
import discord
from settings import TOKEN

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


voice = None
@client.event
async def on_message(message):
    global voice
    if message.author.id == 461173185916960768 or message.author.id == 467398633755770890 and message.content =='!quit':
        sys.exit()

    if message.content == '!join':
        channel = message.author.voice.channel
        print(message.author.id)
        voice = await channel.connect(timeout=10.0,reconnect=True)
    
    if message.content == '!play':
        voice.play(discord.FFmpegPCMAudio('1.mp3'), after=None)
    

    if message.content == '!pause' and voice.is_playing():
        voice.pause()

    
    if message.content == '!resume' and voice.is_paused():
        voice.resume()

    if message.content == '!stop':
        voice.stop()


    if message.content == '!disconnect':
        await voice.disconnect(force=False)



client.run(TOKEN)