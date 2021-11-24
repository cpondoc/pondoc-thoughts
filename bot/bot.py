# Creates a bot to stream my thoughts
import os
import discord
from dotenv import load_dotenv
import random
from tinydb import TinyDB, Query

# Load in token
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
    # Return automatically if bot; else, infinite loop
    if message.author == client.user:
        return
        
    # Printing information about the message content
    print("Channel: " + str(message.channel))
    print("Content: " + str(message.content))
    
    # Insert into database
    db.insert({'channel': str(message.channel), 'content': str(message.content)})

    # Response back to user
    await message.channel.send('Reflection received :)')

# Run the code
client.run(TOKEN)