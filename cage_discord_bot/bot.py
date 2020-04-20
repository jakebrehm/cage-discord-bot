import asyncio
import json
import os
import pathlib
import random

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def clear(context, amount=5):
    await context.channel.purge(limit=amount+1)

@client.command()
async def kick(context, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await context.send(f"Kicked {member.mention}.")

@client.command()
async def ban(context, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await context.send(f"Banned {member.mention}.")

@client.command()
async def unban(context, *, member):
    banned_users = await context.guild.bans()
    name, discriminator = member.split('#')

    for banned_user in banned_users:
        user = banned_user.user
        if (user.name, user.discriminator) == (name, discriminator):
            await context.guild.unban(user)
            await context.send(f"Unbanned {user.mention}.")
            return

@client.command()
async def ping(context):
    await context.send("Don't worry, I'm here.")

@client.command(aliases=['fact', 'fun-fact'])
async def funfact(context):
    PROJECT_DIRECTORY = pathlib.Path(__file__).parent.parent
    DATA_FOLDER = os.path.join(PROJECT_DIRECTORY, 'data')
    FUN_FACTS = os.path.join(DATA_FOLDER, 'facts.json')
    with open(FUN_FACTS, 'r') as json_file:
        facts = json.load(json_file)
    await context.send(random.choice(facts))

@client.event
async def on_message(message):
    deformatted = message.content.lower().replace(' ', '')
    name, discriminator = message.author.name, message.author.discriminator
    if all(s in deformatted for s in ['who', 'nic', 'cage']):
        await message.channel.send(f"That's ridiculous, {name}. Goodbye.")
        await asyncio.sleep(2)
        await message.author.kick(reason=f"{name} was being absurd.")
        await asyncio.sleep(1)
        await message.channel.send("That was ugly. I'm sorry, everyone.")
    await client.process_commands(message)


if __name__ == '__main__':

    import configparser

    # Use pathlib and os to get the path of the project folder
    PROJECT_DIRECTORY = pathlib.Path(__file__).parent.parent
    DATA_FOLDER = os.path.join(PROJECT_DIRECTORY, 'data')

    # Read the configuration file
    config = configparser.ConfigParser()
    CONFIG_PATH = os.path.join(DATA_FOLDER, 'config.ini')
    config.read(CONFIG_PATH)

    # Read the token information and start the bot
    token = config['authorization']['token']
    client.run(token)
