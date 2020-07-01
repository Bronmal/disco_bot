import os
import discord
import settings
import player
import zaycev


client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


voice = None
player_ = None
@client.event
async def on_message(message):

    global voice
    global player_
    if message.content == '!join':
        channel = message.author.voice.channel
        voice = await channel.connect(timeout=10.0,reconnect=True)
    
    if message.content == '!disconnect':
        voice.disconnect(force=False)

    if message.content.startswith('!play'):
        player_ = player.Player(voice)
        zay = zaycev.Zaycev()

        path_song = zay.download(message.content[6:])
        os.chdir(path_song)
        player_.play_track(os.listdir()[0])
        await message.channel.send(f'Трек "{message.content[6:]}" включен!')


    if message.content.startswith('!play_list'):
        player_ = player.Player(voice)
        zay = zaycev.Zaycev()

        path_song = zay.download(message.content[6:])
        os.chdir(path_song)
        player_.play_list(os.listdir())

    if message.content == '!stop':
        player_.stop()
        await message.channel.send('Трек выключен!')




client.run(settings.TOKEN)