import discord
from discord.ext import commands
import asyncio
import hashlib
import random

class Vibe(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command('vibe', desc = ['Perform a vibe check.', '- Check your own vibe', '@user - Check <user>\'s vibe'],
            min = 0, max = float('inf'), category = 'Fun')
    async def vibe(self, ctx, target : discord.Member = None):

        vibes = [':crown: Royalty', ':woman_artist: Artsy', ':full_moon_with_face: Strange', ':rose: Charming', ':boxing_glove: Chutzpah',
            ':coffee: Cozy', ':skull: Cursed', ':chocolate_bar: Ravenous']

        if target is None:
            target = ctx.author

        resp = await ctx.send('🔮 | Checking **{}**\'s vibe...'.format(target))
        await asyncio.sleep(4.0)

        hash = hashlib.sha256()
        hash.update(target.id.to_bytes(8, 'big'))

        values = [x % 100 for x in list(hash.digest())[7:15]]

        for i, v in enumerate(values):
            values[i] = int(max(min(v + random.gauss(0, 10), 100), 0))

        if values[4] > 66 or any(v > 80 for v in values) or values[3] > 60 or values[6] < 20:
            desc = ':white_check_mark: **| Vibe check passed**'

        else:
            desc = ':no_entry_sign: **| Vibe check failed**'

        embed = discord.Embed(title = 'Vibe Check', description = desc, color = 0x7ce4f7)
        embed.set_author(name = str(target), icon_url = target.avatar_url)
        embed.set_footer(text = 'Checked by {}'.format(ctx.author), icon_url = ctx.author.avatar_url)

        for vibe, value in zip(vibes, values):
            bars = int((value/100.0)*10)
            embed.add_field(name = '**{} | {}% |**'.format(vibe, value), inline = False,
                            value = '|' + '▬'*bars + ':radio_button:' + '▬'*(10-bars) + '|')

        await resp.edit(content = '', embed = embed)

# Connect cog to bot
def setup(bot):
    bot.add_cog(Vibe(bot))