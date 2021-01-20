import discord
from discord.ext import commands
import random

class EightBall(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    # * is a wildcard: allows multiple arguments to be passed in
    async def eightball(self, ctx, *, question = None):
        if ctx.author == bot.user:
            return
    
        if question == None:
            await ctx.send("You have to ask a question!")
        else:
            responses = [
                'The stars will most definitely grant your wish!',
                'The stars in the milky way are blinking in a decidedly good fashion!',
                '01111001 01100101 01110011',
                'You may rely on it.',
                'Concentrate and ask again!',
                'Beep boop, cannot predict now.',
                'My hacking sources say not likely!',
                '01101110 01101111',
                'Outlook not so good!',
                'Don\'t count on it.'
            ]

            response = random.choice(responses)
            await ctx.send(response)

def setup(bot):
    bot.add_cog(EightBall(bot))