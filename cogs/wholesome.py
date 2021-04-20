import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import praw
import urllib
import argparse
import pandas as pd
import datetime
from bs4 import BeautifulSoup
import requests
import random

load_dotenv()
cid = os.getenv('REDDIT_CLIENT_ID')
csecret = os.getenv('REDDIT_CLIENT_SECRET')
agent = os.getenv('REDDIT_USER_AGENT')
reddit_username = os.getenv('reddit_name')
reddit_pass = os.getenv('reddit_pass')

class Wholesome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['wholesome'])
    async def wholesomememes(self, ctx):
        reddit = praw.Reddit(client_id = cid,
                             client_secret = "Lta6PV6grSbsJfXWC1HtC93jmN4",
                             username = reddit_username,
                             password = reddit_pass,
                             user_agent = agent)

        subreddit = reddit.subreddit('wholesomememes')
        posts = subreddit.hot(limit=50)
        all_posts = []

        for post in posts:
            all_posts.append(post)
            
        random_post = random.choice(all_posts)

        title = random_post.title
        url = random_post.url

        embed = discord.Embed(title = title, color=0x7ce4f7, timestamp=ctx.message.created_at)
        embed.set_image(url = url)
        embed.set_footer(text=f"Requested by {ctx.author.name}")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Wholesome(bot))