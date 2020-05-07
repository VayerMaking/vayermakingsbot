import discord
from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("bot is online")

    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a+b)

    @commands.command()
    async def multilpy(self, ctx, a: int, b: int):
        await ctx.send(a*b)

    @commands.command()
    async def greet(self, ctx):
        await ctx.send(":smiley: :wave: Hello, there!")

    @commands.command()
    async def cat(self, ctx):
        await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

        # give info about you here
        embed.add_field(name="Author", value="VayerMaking")

        # Shows the number of servers the bot is member of.
        embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

        # give users a link to invite thsi bot to their server
        embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=691320545202929694&permissions=8&scope=bot")

        await ctx.send(embed=embed)

    bot.remove_command('help')

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

        embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
        embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
        embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
        embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
        embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
        embed.add_field(name="$help", value="Gives this message", inline=False)
        embed.add_field(name="$host", value="Gives host IP address", inline=False)
        embed.add_field(name="$players_online", value="Shows who's online now in the server", inline=False)
        embed.add_field(name="$ping", value="Shows the latency of the server", inline=False)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Basic(client))
