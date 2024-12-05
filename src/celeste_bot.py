import discord
import re
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check if the message starts with the command prefix
    if message.content.startswith('!price'):
        # Extract the number from the message
        match = re.search(r'\d+', message.content)
        if match:
            number = match.group(0)
            response = f"{message.author.name}'s Island is currently reporting a turnip price of {number} bells."
            await message.channel.send(response)
        else:
            await message.channel.send('Please provide a number after the command.')

client.run(os.environ['CELESTE_BOT_TOKEN'])