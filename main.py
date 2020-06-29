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
    if message.author == client.user:
        return

    if message.content == '!join':
        channel = message.author.voice.channel
        voice = await channel.connect(timeout=10.0,reconnect=True)

    if message.content == '!disconnect':
        await voice.disconnect(force=False)



client.run(TOKEN)