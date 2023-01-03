import discord
from discord.ext import commands
import random

class ShakespeareInsults(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    # @commands.command()
    # async def insult(self, ctx):
        
async def setup(bot):
    await bot.add_cog(ShakespeareInsults(bot))