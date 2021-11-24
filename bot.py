# Creates a bot to stream my thoughts
import os
import discord
from dotenv import load_dotenv
import random
from tinydb import TinyDB, Query

# Need to figure out how this works -- getting os env stuff
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up client and db
client = discord.Client()
db = TinyDB('data/db.json')

# Checks that the bot has opened
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# Looking at important message information
@client.event
async def on_message(message):
    # Printing information about the message content
    print("Channel: " + str(message.channel))
    print("Content: " + str(message.content))
    
    # Insert into database
    db.insert({'channel': str(message.channel), 'content': str(message.content)})
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

client.run(TOKEN)