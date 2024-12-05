import discord
from discord.ext import commands
from discord import app_commands
import os
from constants import TURNIP_CHANNEL_ID, METEOR_CHANNEL_ID

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
    response = f"I'm not usually one to gossip, but I hear <@{interaction.user.id}> Island is currently buying turnips for **{price} bells.**"
    target_channel = bot.get_channel(int(TURNIP_CHANNEL_ID))
    if target_channel:
        await target_channel.send(response)
        await interaction.response.send_message(f"Oh, hello! I'll put that turnip report in {target_channel.mention}", ephemeral=True)
    else:
        await interaction.response.send_message('ERROR_LOG: Target channel not found.', ephemeral=True)
        
@bot.tree.command(name="stars", description="Report meteor shower")
@app_commands.describe(stars="The meteor shower information")
async def stars(interaction: discord.Interaction, stars: str = None):
    if stars is None or stars.lower() == "normal":
        response = f"🌠 I'm not usually one to gossip, but I hear <@{interaction.user.id}> Island is currently experiencing a meteor shower. 🌠"
    elif stars.lower() == "heavy":
        response = f"🌠 I'm not usually one to gossip, but I hear <@{interaction.user.id}> Island is currently experiencing a **HEAVY** meteor shower. 🌠"
    else:
        await interaction.response.send_message("Oh, I'm sorry, I don't understand.\nYou can tell me nothing and I will say its a small meteor shower or you can say:\nnormal\nheavy", ephemeral=True)
    target_channel = bot.get_channel(int(METEOR_CHANNEL_ID))
    if target_channel:
        await target_channel.send(response)
        await interaction.response.send_message(f"Oh, hello! I'll put that weather report in {target_channel.mention}", ephemeral=True)
    else:
        await interaction.response.send_message('ERROR_LOG: Target channel not found.', ephemeral=True)

@bot.tree.command(name="help", description="Show help information")
async def help_command(interaction: discord.Interaction):
    response = f"Oh, yes, hello! I respond to the following commands:\n/stars <optional: 'normal' or 'heavy'>\n/turnip <price>\n/help"
    await interaction.response.send_message(response, ephemeral=True)

bot.run(os.environ['CELESTE_BOT_TOKEN'])