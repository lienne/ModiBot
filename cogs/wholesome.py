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

load_dotenv()
api_key = os.getenv('REDDIT_API_KEY')
client_id = os.getenv('REDDIT_CLIENT_ID')
user_agent = os.getenv('REDDIT_USER_AGENT')

class Wholesome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # def wholesomememes(self, ctx):
    #     reddit = praw.Reddit(cid = client_id, csecret = api_key, agent = user_agent)
    #     subreddit = reddit.subreddit('wholesomememes')
    #     posts = subreddit.hot(limit=10)

    #     allowed_img_extensions = ['.jpg', '.jpeg', '.png']
    #     img_urls = []
    #     img_titles = []

    #     for post in posts:
    #         img_urls.append(post.url.encode('utf-8'))
    #         img_titles.append(post.title.encode('utf-8'))
            

    #     for index, url in enumerate(img_urls):
    #         _, ext = os.path.splitext(img_urls)

    #         if ext in allowed_img_extensions:
    #             try:
    #                 print('downloading ' + img_urls[index])
    #                 urllib.urlretrieve(img_urls[index])
                    
def setup(bot):
    bot.add_cog(Wholesome(bot))