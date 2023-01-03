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

start = dt.fromtimestamp(1602284400, tz = est) # 6pm Oct 9th 2020
end = dt.fromtimestamp(1602442800, tz = est) # 3pm Oct 11th 2020

orl = partial(dt.now, tz = est) # Gives current time in Orlando

# Schedule Oct 9-11, 2020
# sched = {
#     9: [
#         ('5:00pm - 7:00pm', 'Hopin Open', ''),
#         ('7:00pm - 8:00pm', 'Opening Ceremony', ''),
#         ('8:00pm - 10:00pm', 'Virtual Career Fair', ''),
#         ('10:00pm', 'Hacking Starts', ''),
#         ('10:00pm - 10:30pm', 'Team Building', ''),
#         ('10:00pm - 11:00pm', 'Google Sponsor Workshop 1', ''),
#         ('11:00pm - 12:00am', 'Help! I\'ve Never Programmed Before!', ''),
#         ('12:00am - 1:00am', 'Intro to Hackathons', ''),
#         ('1:00am - 2:00am', 'Among Us', '')
#     ],
#     10: [
#         ('7:00am - 8:00am', 'Morning Coffee & Networking', ''),
#         ('8:00am - 9:00am', 'CTF', ''),
#         ('9:00am - 10:00am', 'The Greatest Intro to JavaScript', ''),
#         ('10:00am - 11:00am', 'Intro to Python', ''),
#         ('10:00am - 11:00am', 'Intro to Angular', ''),
#         ('11:00am - 12:00pm', 'Intro to Azure', ''),
#         ('12:00pm - 1:00pm', 'Intro to LaTeX', ''),
#         ('1:00pm - 3:00pm', 'Intro to ML w/ AI@UCF', ''),
#         ('1:00pm - 1:30pm', 'Origami Break', ''),
#         ('1:00pm - 2:00pm', 'Becoming a Software Engineer', ''),
#         ('2:00pm - 3:00pm', 'Intro to AR', ''),
#         ('2:00pm - 3:00pm', 'Coffee Break & Networking', ''),
#         ('2:00pm - 4:00pm', 'Git it Together', ''),
#         ('3:00pm - 4:00pm', 'Ladies Storm Hackathon', ''),
#         ('4:00pm - 4:30pm', 'Analyzing FOREX Market Conditions with Machine Learning', ''),
#         ('4:00pm - 5:00pm', 'Yoga with RWC', ''),
#         ('4:00pm - 6:00pm', 'AR in Unity', ''),
#         ('4:30pm - 5:00pm', 'Interview Prep', ''),
#         ('5:00pm - 6:00pm', 'Functional Programming', ''),
#         ('5:00pm - 6:15pm', 'Search Engines', ''),
#         ('6:00pm - 7:00pm', 'Web App Security Testing with Burp Suite', ''),
#         ('6:00pm - 7:00pm', 'Write a Discord Bot in Python', ''),
#         ('6:30pm - 7:00pm', 'Animal Crossing Island Hopping', ''),
#         ('7:00pm - 8:00pm', 'Intro to Adobe XD', ''),
#         ('8:00pm - 9:00pm', 'Sponsor Office Hours', ''),
#         ('10:00pm - 11:00pm', 'Karaoke', ''),
#         ('11:00pm - 12:00am', 'Werewolf', ''),
#         ('12:00am - 1:00am', 'Among Us', '')
#     ],
#     11: [
#         ('10:00am', 'Hacking Ends', ''),
#         ('10:00am - 12:00pm', 'Demo Devpost Prep', ''),
#         ('12:00pm - 2:00pm', 'Judging', ''),
#         ('2:00pm - 3:00pm', 'Closing Ceremony', '')
#     ]
# }

sched = {
    9: [
        ('5:00 pm', 'Hopin Open - 5pm EDT', ''),
        ('7:00 pm', 'Opening Ceremony - 7pm EDT', ''),
        ('8:00 pm', 'Virtual Career Fair - 8pm EDT', 'https://app.hopin.to/events/knight-hacks/expo'),
        ('10:00 pm', 'Hacking Starts - 10pm EDT', ''),
        ('10:00 pm', 'Team Building - 10pm EDT', ''),
        ('10:00 pm', 'Welcome To Cloud Hero Data & ML with BigQuery - 10pm EDT', ''),
        ('11:00 pm', 'Help! I\'ve Never Programmed Before! - 11pm EDT', ''),
        ('11:59 pm', 'HACK 101: Hackathon Fundamentals - 12am EDT', ''),
    ],
    10: [
        ('1:00 am', 'Among Us - 1am EDT', ''),
        ('7:00 am', 'Morning Coffee & Networking - 7am EDT', ''),
        ('8:00 am', 'Skribbl.io - 8am EDT', ''),
        ('9:00 am', 'The Greatest Intro to JavaScript - 9am EDT', ''),
        ('10:00 am', 'A Crash Course in Python Development - 10am EDT', ''),
        ('10:00 am', 'Intro to Angular - 10am EDT', ''),
        ('11:00 am', 'Azure Backend Workshop - 11am EDT', ''),
        ('11:00 am', 'Microsoft Paint Bob Ross', ''),
        ('12:00 pm', 'US Air Force Capture the Flag challenge with MLH', ''),
        ('12:00 pm', 'Intro to LaTeX with ACM/ACM-W - 12pm EDT', ''),
        ('1:00 pm', 'Intro to ML w/ AI@UCF - 1pm EDT', ''),
        ('1:00 pm', 'Origami Break - 1pm EDT', ''),
        ('1:00 pm', 'Boring AI??? Continuous Learning Overview w/ PWC', ''),
        ('1:00 pm', 'Becoming a Software Engineer - 1pm EDT', ''),
        # ('2:00 pm', 'Intro to AR - 2pm EDT', ''),
        ('2:00 pm', 'Coffee Break & Networking - 2pm EDT', ''),
        ('2:00 pm', 'Git it Together - 2pm EDT', ''),
        ('3:00 pm', 'Ladies Storm Hackathons - 3pm EDT', ''),
        ('3:00 pm', 'Human-Computer Interaction: The Woolly Mammoth Story - 3pm EDT', ''),
        ('4:00 pm', 'AR in Unity - 4pm EDT', ''),
        ('4:00 pm', 'Yoga with RWC - 4pm EDT', ''),
        ('4:00 pm', 'Analyzing FOREX Market Conditions with Machine Learning - 4pm EDT', ''),
        ('4:30 pm', 'Search Engines - 4:30pm EDT', ''),
        ('5:00 pm', 'Functional Programming - 5pm EDT', ''),
        ('6:00 pm', 'Write a Discord Bot in Python - 6pm EDT', ''),
        ('6:00 pm', 'Web App Security Testing with Burp Suite - 6pm EDT', ''),
        ('6:30 pm', 'Animal Crossing Island Hopping - 6:30pm EDT', ''),
        ('7:00 pm', 'Intro to Adobe XD - 7pm EDT', ''),
        ('7:00 pm', 'Army Workshop: We Are PEO STRI!', ''),
        ('8:00 pm', 'Sponsor Office Hours - 8pm EDT', ''),
        ('8:00 pm', 'Werewolf - 8pm EDT', ''),
        ('9:00 pm', 'Interview Prep - 9pm EDT', ''),
        ('10:00 pm', 'Karaoke - 10pm EDT', ''),
        ('11:00 pm', 'Among Us - 11pm EDT', '')
    ],
    11: [
        # ('12:00 am', 'Among Us - 12am EDT', ''),
        ('10:00 am', 'Hacking Ends - 10am EDT', ''),
        ('10:00 am', 'Demo Devpost Prep - 10am EDT', ''),
        ('12:00 pm', 'Judging Starts - 12pm EDT', ''),
        ('2:00 pm', 'Closing Ceremony - 2pm EDT', '')
    ]
}

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

    @commands.command()
    async def schedule(self, ctx):
        embeds = []

        for day, events in sched.items():
            if day >= orl().day:
                full_day = ['Friday', 'Saturday', 'Sunday'][day - 9]

                embed = discord.Embed(title = 'KnightHacks 2020 Schedule :scroll:',
                                      description = f'**{full_day}, Oct {day}** \nAll Workshops are on Hopin! \nSo much fun to be had :))',
                                      color = 0x7ce4f7)

                for num, event in enumerate(events):
                    event_time, event_name, link = event
                    left = dt.strptime(f"2020 Oct {day} {event_time}", "%Y %b %d %I:%M %p").replace(tzinfo=est)
                    if (left > orl()):
                        embed.add_field(name=f"{num + 1}. {event_name}",
                                    value=(f"in {time_left(left)}" + (f", [**link**]({link})" if link else '')),
                                    inline=False)

                embeds.append(embed)

        await paginate_embed(self.bot, ctx.channel, embeds)

async def setup(bot):
    await bot.add_cog(Times(bot))