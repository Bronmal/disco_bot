import sys
import os
import discord
from settings import TOKEN


client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


voice = None
search_word = None

@client.event
async def on_message(message):
    global voice
    global search_word
    if (message.author.id == 461173185916960768 or message.author.id == 467398633755770890) and message.content =='!quit':
        sys.exit()

    if message.content == '!join':
        channel = message.author.voice.channel
        voice = await channel.connect(timeout=10.0,reconnect=True)
    
    if message.content.startswith('!play'):
        search_word = message.content[6:]
        search_word = search_word.replace(' ', '+')
        os.chdir(path)

        player = Player(voice=voice, client=client, search_word=search_word)

        player.play()

        '''try:
            voice.play(discord.FFmpegPCMAudio(os.listdir(path)[os.listdir(path).index(search_word + '0' + '.mp3')]), after=None)

        except:
            download_zay(search_word)
            voice.play(discord.FFmpegPCMAudio(os.listdir(path)[os.listdir(path).index(search_word + '0' + '.mp3')]), after=None)'''

    if message.content == '!pause' and voice.is_playing():
        voice.pause()
        voice.is_done()

    
    if message.content == '!resume' and voice.is_paused():
        voice.resume()

    if message.content == '!stop':
        voice.stop()


    if message.content == '!disconnect':
        await voice.disconnect(force=False)



client.run(TOKEN)