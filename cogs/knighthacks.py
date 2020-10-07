import discord
from discord.ext import commands
import random

class KnightHacks(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def github(self, ctx):
        await ctx.send("closed source for now bb")

    @commands.command()
    async def why(self, ctx):
        await ctx.send("<:yeehaw:762850304781189161>")

    @commands.command()
    async def how(self, ctx):
        await ctx.send("Hacker guide link coming soon.")

    @commands.command()
    async def what(self, ctx):
        await ctx.send("bro idk")

    @commands.command()
    async def who(self, ctx):
        responses = [
            '...let the dogs out! WHO WHO WHO WHO WHO!',
            '...stole the cookie from my cookie jar?',
            '...ate my ramen?!'
        ]
        
        response = random.choice(responses)
        await ctx.send(response)

    @commands.command()
    async def reee(self, ctx):
        await ctx.send("<:reeeee:763240777525493850>")

    @commands.command()
    async def REEE(self, ctx):
        await ctx.send("<:ultrareee:763241316451876896>")

def setup(bot):
    bot.add_cog(KnightHacks(bot))