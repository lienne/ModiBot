'''
Credit for this code goes to Aadi, from VandyHacks!
Check him out: https://github.com/aadibajpai
'''


from datetime import timedelta, timezone as tz, datetime as dt
from functools import partial

from utils import paginate_embed

import discord
from discord.ext import commands

#est is 4hrs ahead of utc
est = tz(timedelta(hours = -4))

start = dt.fromtimestamp(1602280800, tz = est) # 6pm Oct 9th 2020
end = dt.fromtimestamp(1602442800, tz = est) # 3pm Oct 11th 2020

orl = partial(dt.now, tz = est) # Gives current time in Orlando

def time_left(event):
    diff = event - orl()
    d = diff.days
    h, m = divmod(diff.seconds, 3600)
    m, s = divmod(m, 60)

    return (f"{d} day{'s' * bool(d - 1)}, " if d else "") \
           + (f"{h} hour{'s' * bool(h - 1)}, " if h else "") \
           + (f"{m} minute{'s' * bool(m - 1)} and " if m else "") \
           + f"{s} second{'s' * bool(s - 1)}"

class Times(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def when(self, ctx):
        if start > orl():
            event = start
        else:
            event = end

        if orl() > end:
            breakdown = "hackathon over come back next year :))"
        else:
            breakdown = "KnightHacks " \
                + ("begins " if start > orl() else "ends ") \
                + "in " + time_left(event) + " bb"

        await ctx.send(breakdown)

def setup(bot):
    bot.add_cog(Times(bot))