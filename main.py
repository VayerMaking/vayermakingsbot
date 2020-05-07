import discord
from discord.ext import commands
import config
import os

bot = commands.Bot(command_prefix = '$')

initial_extensions = ['cogs.basic','cogs.minecraft','cogs.reactions']
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="хората в KurKuma"))
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')


bot.run(config.token)
