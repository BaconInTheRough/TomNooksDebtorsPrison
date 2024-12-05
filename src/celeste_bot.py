import discord
import re
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

valid_commands = [
    '!help',
    '!turnip',
    ]

@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check if the message starts with the command prefix
    if message.content.startswith('!turnip'):
        # Extract the number from the message
        match = re.search(r'\d+', message.content)
        if match:
            number = match.group(0)
            response = f"I'm not usually one to gossip but I hear @{message.author.name} Island is currently reporting a turnip price of {number} bells."
            await message.channel.send(response)
        else:
            await message.channel.send('Please provide a number after the command.')
    if message.content.startswith('!help'):
        response = f"Oh, yes, hello! I respond to: {', '.join(valid_commands)}"
        await message.channel.send(response)

client.run(os.environ['CELESTE_BOT_TOKEN'])