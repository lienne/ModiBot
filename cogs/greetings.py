import discord
from discord.ext import commands

"""
Currently unnecessary command for KnightHacks 2020.
"""

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    # @commands.Cog.listener()
    # async def on_member_join(self, member):
    #     channel = member.guild.system_channel
    #     if channel is not None:
    #         await channel.send('Hello, {0.mention}, welcome to the server!'.format(member))
        
    #     @commands.command()
    #     async def hello(self, ctx, *, member: discord.Member = None):
    #         """Say hello"""
    #         member = member or ctx.author
    #         if self._last_member is None or self._last_member.id != member.id:
    #             await ctx.send('Hello, {0.mention}, welcome to the server!'.format(member))
    #         else:
    #             await ctx.send('Hi {0.name}... This feels familiar.'.format(member))
    #         self._last_member = member

def setup(bot):
    bot.add_cog(Greetings(bot))