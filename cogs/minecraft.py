import discord
from discord.ext import commands
from mcstatus import MinecraftServer
import json


bot = commands.Bot(command_prefix='.')
host_ip = "34.91.53.97:25565"
server = MinecraftServer.lookup(host_ip)

data = {'online': False}
data['players'] = []


class Minecraft(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ping(self, ctx):
        latency = server.ping()
        embed = discord.Embed(title="Pinging...", color=0xeee657)
        embed.add_field(name="Latency", value=latency)
        await ctx.send(embed=embed)

    @commands.command()
    async def host(self, ctx):
        embed = discord.Embed(title="Latest Host IP", color=0xeee657)
        embed.add_field(name="IP", value=host_ip)
        await ctx.send(embed=embed)


    @commands.command()
    async def player_online(self, ctx):
        status = server.status()
        b = [
                    "{} ({})".format(player.name, player.id)
                    for player in status.players.sample
                ] if status.players.sample is not None else "No players online"
        #print(b)
        a = " {}/{} ".format(status.players.online,status.players.max)
        embed = discord.Embed(title="Searching For Online Players...", color=0xeee657)
        embed.add_field(name="online", value=a)
        embed.add_field(name="player", value=b)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Minecraft(client))
