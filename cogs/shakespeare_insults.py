import discord
from discord.ext import commands
import random

class ShakespeareInsults(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def insult(self, ctx):
        list1 = [
            'artless',
            'bawdy',
            'beslubbering',
            'bootless',
            'bumbling',
            'churlish',
            'cockered',
            'clouted',
            'craven',
            'currish',
            'dankish',
            'dissembling',
            'droning',
            'errant',
            'fawning',
            'fobbing',
            'froward',
            'frothy',
            'gleeking',
            'goatish',
            'gorbellied',
            'impertinent',
            'infectious',
            'jarring',
            'loggerheaded',
            'lumpish',
            'mammering',
            'mangled',
            'mewling',
            'paunchy',
            'pribbling',
            'puking',
            'puny',
            'qualling',
            'rank',
            'reeky',
            'roguish',
            'ruttish',
            'saucy',
            'spleeny',
            'spongy',
            'surly',
            'tottering',
            'unmuzzled',
            'vain',
            'venomed',
            'villainous',
            'warped',
            'wayward',
            'weedy',
            'yeasty'
        ]

        list2 =[
            'base-court',
            'bat-fowling',
            'beef-witted',
            'beetle-headed',
            'boil-brained',
            'clapper-clawed',
            'clay-brained',
            'common-kissing',
            'crook-patted',
            'dim-witted',
            'dismal-dreaming',
            'dizzy-eyed',
            'doghearted',
            'dread-bolted',
            'earth-vexing',
            'elf-skinned',
            'fat-kidneyed',
            'fen-sucking',
            'flap-mouthed',
            'fly-bitten',
            'folly-fallen',
            'fool-born',
            'full-gorged',
            'guts-griping',
            'half-faced',
            'hasty-witted',
            'hedge-born',
            'hell-hated',
            'idle-headed',
            'ill-bred',
            'ill-breeding',
            'ill-nurtured',
            'knotty-patted',
            'milk-livered',
            'motley-minded',
            'onion-eyed',
            'plume-plucked',
            'pottle-deep',
            'pox-marked',
            'reeling-ripe',
            'rough-hewn',
            'rude-growing',
            'rump-fed',
            'shard-borne',
            'sheep-biting',
            'spur-galled',
            'swag-bellied',
            'tardy-gaited',
            'tickle-brained',
            'toad-spotted',
            'urchin-snouted',
            'weather-bitten'
        ]

        list3 = [
            'apple-john',
            'baggage',
            'barnacle',
            'bladder',
            'boar-pig',
            'bugbear',
            'bum-bailey',
            'canker-blossom',
            'clack-dish',
            'clotpole',
            'coxcomb',
            'codpiece',
            'death-token',
            'dewberry',
            'flap-dragon',
            'flax-wench',
            'flirt-gill',
            'foot-licker',
            'fustilarian',
            'giglet',
            'gudgeon',
            'haggard',
            'harpy',
            'hedge-pig',
            'horn-beast',
            'hugger-mugger',
            'joithead',
            'lewdster',
            'lout',
            'maggot-pie',
            'malt-worm',
            'mammet',
            'measle',
            'minnow',
            'miscreant',
            'moldwarp',
            'mumble-news',
            'nut-hook',
            'pidgeon-egg',
            'pignut',
            'puttock',
            'pumpion',
            'ratsbane',
            'scut',
            'skainsmate',
            'strumpet',
            'varlot',
            'vassal',
            'whey-face'
            'wagtail'
        ]

        insult1 = random.choice(list1)
        insult2 = random.choice(list2)
        insult3 = random.choice(list3)

        await ctx.send("Thou " + insult1 + " " + insult2 + " " + insult3 + "!")
        
async def setup(bot):
    await bot.add_cog(ShakespeareInsults(bot))