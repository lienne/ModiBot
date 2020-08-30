import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
MSGID = os.getenv('TRUSTED_ROLES_MSG_ID')

class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def on_raw_reaction_add(payload):
        message_id = payload.message_id
        if message_id == MSGID:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

            if payload.emoji.name == 'rooDevil':
                role = discord.utils.get(guild.roles, name = 'manager')
            elif payload.emoji.name == 'smugcat4':
                role = discord.utils.get(guild.roles, name = 'trans')
            else:
                role = discord.utils.get(guild.roles, name = payload.emoji.name)
            
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print('Done.')
            else:
                print('Role not found.')


    @bot.event
    async def on_raw_reaction_remove(payload):
        message_id = payload.message_id
        if message_id == MSGID:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

            if payload.emoji.name == 'rooDevil':
                role = discord.utils.get(guild.roles, name = 'manager')
            elif payload.emoji.name == 'smugcat4':
                role = discord.utils.get(guild.roles, name = 'trans')
            else:
                role = discord.utils.get(guild.roles, name = payload.emoji.name)
            
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print('Done.')
            else:
                print('Role not found.')

# Connect cog to bot
def setup(bot):
    bot.add_cog(Roles(bot))