import discord
from discord.ext import commands
class Links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["links", "membership-dues", "feedback", "fees", "ops"])
    async def khlinks(self, ctx):
        links = ("[Find current events happening this week!](https://knighthacks.org/linktree)" +
            "\n\n[Pay your dues](https://knighthacks.org/dues)\n\n" +
            "[Give feedback on a specific workshop](https://knighthacks.org/feedback)\n\n" +
            "[Sign up to be a Knight Hacks club member](https://knighthacks.org/membership)\n\n" + 
            "[Come to our ops meeting](https://knighthacks.org/ops)")

        await ctx.send(
                        f"{ctx.author.mention}"
        )
        embed = discord.Embed(color=0x7ce4f7, timestamp=ctx.message.created_at)
        embed.add_field(name="KnightHacks links", value=links)
        embed.set_thumbnail(url = "https://github.com/lienne/ModiBot/blob/master/cogs/img/headphonesdog.png?raw=true")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Links(bot))