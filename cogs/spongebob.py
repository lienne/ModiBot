import discord
from discord.ext import commands

class Spongebob(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['mock', 'sponge'])
    async def spongebob(self, ctx):
        pass
        # await ctx.channel.send

def setup(bot):
    bot.add_cog(Spongebob(bot))