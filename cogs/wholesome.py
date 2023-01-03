import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncpraw
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
        async with asyncpraw.Reddit(client_id = cid,
                             client_secret = csecret,
                             username = reddit_username,
                             password = reddit_pass,
                             user_agent = agent) as reddit:

            subreddit = await reddit.subreddit('wholesomememes')
            all_posts = []
            async for submission in subreddit.hot(limit=50):
                all_posts.append(submission)
                
            random_post = random.choice(all_posts)

            title = random_post.title
            url = random_post.url

            embed = discord.Embed(title = title, color=0x7ce4f7, timestamp=ctx.message.created_at)
            embed.set_image(url = url)
            embed.add_field(name="url", value=url)
            embed.set_footer(text=f"Requested by {ctx.author.name}")

            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Wholesome(bot))