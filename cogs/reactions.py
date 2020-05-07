import discord
from discord.ext import commands
import config

class Reactions(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == config.your_message_id:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda  g : g.id == guild_id, bot.guilds)
            #here you add the emoji name in the if/else statement and add the role name after name='
            if payload.emoji.name == 'nekvi_zaeti':
                role = discord.utils.get(guild.roles, name='nekvi_zaeti')
            elif payload.emoji.name == 'samotnitzi_bez_jena':
                role = discord.utils.get(guild.roles, name='samotnitzi_bez_jena')
            elif payload.emoji.name == 'samotni4ki_bez_muz':
                role = discord.utils.get(guild.roles, name='samotni4ki_bez_muz')
            elif payload.emoji.name == 'minecrafteri':
                role = discord.utils.get(guild.roles, name='minecrafteri')
            elif payload.emoji.name == 'dev':
                role = discord.utils.get(guild.roles, name='dev')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                pass
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    pass
                else:
                    pass
            else:
                pass
        @commands.Cog.listener()
        async def on_raw_reaction_remove(self, payload):
            message_id = payload.message_id
            if message_id == config.your_message_id:
                guild_id = payload.guild_id
                guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

                if payload.emoji.name == 'nekvi_zaeti':
                    role = discord.utils.get(guild.roles, name='nekvi_zaeti')
                elif payload.emoji.name == 'samotnitzi_bez_jena':
                    role = discord.utils.get(guild.roles, name='samotnitzi_bez_jena')
                elif payload.emoji.name == 'samotni4ki_bez_muz':
                    role = discord.utils.get(guild.roles, name='samotni4ki_bez_muz')
                elif payload.emoji.name == 'maincrafteri':
                    role = discord.utils.get(guild.roles, name='maincrafteri')
                elif payload.emoji.name == 'dev':
                    role = discord.utils.get(guild.roles, name='dev')
                else:
                    role = discord.utils.get(guild.roles, name=payload.emoji.name)

                if role is not None:
                    pass
                    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                    if member is not None:
                        await member.remove_roles(role)
                        pass
                    else:
                        pass
                else:
                    pass



def setup(client):
    client.add_cog(Reactions(client))
