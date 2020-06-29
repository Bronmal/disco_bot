import discord
from settings import TOKEN

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!join'):
        await message.channel.send(message.content)
        channel = message.author.voice.channel
        print(channel.name)
        await channel.connect(timeout=10.0,reconnect=True)

@client.event
async def on_voice_state_update(member,before,after):
    print ('1')



client.run(TOKEN)