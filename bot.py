import os
import logging
import discord
import asyncio

from dotenv import load_dotenv
from discord.ext import commands

class VerifyButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        # self.value = None

    @discord.ui.button(label='Verify', style=discord.ButtonStyle.green, custom_id='verify_button:green')
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Private thread created.', ephemeral=True)
        # self.value = True
        # self.stop()


class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.presences = True
        intents.members = True
        intents.message_content = True

        super().__init__(
            command_prefix = commands.when_mentioned_or('!'),
            help_command=None,
            activity = discord.Game('with the discord API!'),
            intents=intents)

    discord.utils.setup_logging(level=logging.INFO, root=False)

    logger = logging.getLogger('discord')
    logger.setLevel(logging.ERROR)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logger.addHandler(handler)

    async def setup_hook(self) -> None:
        self.add_view(VerifyButton())

    async def on_ready(self):
        print(f'{self.user.name} has joined the chat!')
        print('----------')

bot = MyBot()

@bot.command()
@commands.is_owner()
async def prepare(ctx: commands.Context):
    """Starts a persistent view."""
    # In order for a persistent view to be listened to, it needs to be sent to an actual message.
    # Call this method once just to store it somewhere.
    await ctx.send("Click here to create a new private thread.", view=VerifyButton())

async def main():

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    # GUILD = os.getenv('DISCORD_GUILD')

    @bot.command()
    async def load(ctx, extension):
        await bot.load_extension(f'cogs.{extension}')

    @bot.command()
    async def unload(ctx, extension):
        await bot.unload_extension(f'cogs.{extension}')

    @bot.command()
    async def reload(ctx, extension):
        await bot.unload_extension(f'cogs.{extension}')
        await bot.load_extension(f'cogs.{extension}')

    async with bot:
        # Load all files in cogs folder (remove '.py' from filename when loading)
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')

        await bot.start(TOKEN)

asyncio.run(main())