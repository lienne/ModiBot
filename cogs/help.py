import discord
from discord.ext import commands
import os

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):

        embed = discord.Embed(color=0x7ce4f7)
        embed.set_author(name='Available Commands')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/747214525048160402/754523898699186296/headphonesdog.png')
        embed.set_thumbnail(url='https://github.com/lienne/ModiBot/blob/master/cogs/img/headphonesdog.png?raw=true')
        embed.add_field(name='ping', value='Pong! With latency.', inline=False)
        embed.add_field(name='coinflip', value='Flips a coin.', inline=False)
        embed.add_field(name='diceroll', value='Rolls a die.', inline=False)
        embed.add_field(name='eightball', value='Gives you a prediction to a question.', inline=False)
        embed.add_field(name='vibe', value='Reads a user\'s vibe. If no user is tagged, reads the author\'s vibe.', inline=False)
        embed.add_field(name='whois', value='Displays the specified user\'s info. If no user is tagged, displays the author\'s info.', inline=False)
        embed.add_field(name='stats', value='Displays server info.', inline=False)
        embed.add_field(name='weather', value='Displays specified city\'s current weather.', inline=False)
        embed.add_field(name='cat', value='Displays a random cat.', inline=False)
        embed.add_field(name='dog', value='Displays a random dog.', inline=False)
        embed.add_field(name='fact', value='Displays a random fact.', inline=False)

        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Help(bot))