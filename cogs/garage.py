import discord
from discord.ext import commands
import asyncio
import aiohttp
from bs4 import BeautifulSoup

class Garage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['parking'])
    async def garage(self, ctx):
        complete_url = 'https://secure.parking.ucf.edu/GarageCount/iframe.aspx'

async def setup(bot):
    await bot.add_cog(Garage(bot))