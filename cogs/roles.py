import discord
from discord.ext import commands

class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def on_raw_reaction_add(payload):
        message_id = payload.message_id
        if message_id == 749716013196509264:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

            if payload.emoji.name == 'rooDevil':
                print('manager')
            # role = discord.utils.get(guild.roles, name = )


    @bot.event
    async def on_raw_reaction_remove(payload):
        pass

# Connect cog to bot
def setup(bot):
    bot.add_cog(Roles(bot))