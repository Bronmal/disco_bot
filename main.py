import discord
from discord.ext import commands

import settings

bot = commands.Bot(command_prefix='!')
@bot.command()
async def ping(ctx, arg):
    await ctx.send(arg)

bot.run(settings.TOKEN)