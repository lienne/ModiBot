import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import aiohttp

load_dotenv()
API_KEY = os.getenv('WEATHER_API_KEY')
base_url = "http://api.openweathermap.org/data/2.5/weather?"

class Weather(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weather(self, ctx, *, city: str = ''):
        if city == '':
            await ctx.send('Please specify a city.')
            return

        city_name = city
        complete_url = base_url + 'appid=' + API_KEY + '&q=' + city_name

        async with aiohttp.ClientSession() as session:
            async with session.get(complete_url) as response:
                if response.status != 404:
                    x = await response.json()

            try:
                if x['cod'] != '404':
                    async with ctx.typing():
                        await asyncio.sleep(1)

                        y = x['main']
                        current_temp = y['temp']
                        current_temp_farenheit = str(round((current_temp)*(9/5) - 459.67))
                        feels_like = str(round((y['feels_like'])*(9/5) - 459.67))
                        current_temp_celsius = str(round(current_temp - 273.15))
                        feels_like_C = str(round((y['feels_like']) - 273.15))
                        current_pressure = y['pressure']
                        current_humidity = y['humidity']
                        z = x['weather']
                        weather_description = z[0]['description']

                        embed = discord.Embed(title=f'Weather in {city_name}', color=0x7ce4f7, timestamp=ctx.message.created_at)
                        
                        embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
                        embed.set_footer(text=f"Requested by {ctx.author.name}")

                        embed.add_field(name='Description', value=f'**{weather_description}**', inline=False)
                        embed.add_field(name='Temperature(F)', value=f'**{current_temp_farenheit}°F**', inline=False)
                        embed.add_field(name='Feels Like(F):', value=f'**{feels_like}°F**', inline=False)
                        embed.add_field(name='Temperature(C)', value=f'**{current_temp_celsius}°C**', inline=False)
                        embed.add_field(name='Feels Like(C):', value=f'**{feels_like_C}°C**', inline=False)
                        embed.add_field(name='Humidity(%)', value=f'**{current_humidity}%**', inline=False)
                        embed.add_field(name='Atmospheric Pressure(hPa)', value=f'**{current_pressure}hPa**', inline=False)

                        await ctx.send(embed=embed)

                elif x['cod'] == '404':
                    await ctx.send('City not found.')

            except:
                await ctx.send('City not found.')


async def setup(bot):
    await bot.add_cog(Weather(bot))