import discord
from discord.ext import commands
from discord import app_commands
import os

TURNIP_CHANNEL_ID = '1313380515671314474'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name="turnip", description="Report turnip prices")
@app_commands.describe(price="The turnip price")
async def turnip(interaction: discord.Interaction, price: int):
    response = f"I'm not usually one to gossip but I hear @{interaction.user.name} Island is currently reporting a turnip price of {price} bells."
    target_channel = bot.get_channel(int(TURNIP_CHANNEL_ID))
    if target_channel:
        await target_channel.send(response)
        await interaction.response.send_message(f"Turnip price reported in {target_channel.mention}", ephemeral=True)
    else:
        await interaction.response.send_message('Target channel not found.', ephemeral=True)

@bot.tree.command(name="help", description="Show help information")
async def help_command(interaction: discord.Interaction):
    response = f"Oh, yes, hello! I respond to the following commands:\n/turnip <price>\n/help"
    await interaction.response.send_message(response, ephemeral=True)

bot.run(os.environ['CELESTE_BOT_TOKEN'])