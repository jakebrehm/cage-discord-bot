import asyncio

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def load(context, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(context, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
async def reload(context, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

@client.command()
async def ping(context):
    await context.send("Don't worry, I'm here.")

@client.event
async def on_command_error(context, error):
    name = context.message.author.name
    if isinstance(error, commands.CommandNotFound):
        await context.send(f"I'm not sure what you're asking me to do, {name}.")
    elif isinstance(error, commands.MissingPermissions):
        await context.send(f"Sorry {name}, I can't let you do that.")
    else:
        print(error)

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
    import os

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f"cogs.{filename[:-3]}")

    # Get the path of the data folder
    DATA_FOLDER = os.path.join('..', 'data')

    # Read the configuration file
    config = configparser.ConfigParser()
    CONFIG_PATH = os.path.join(DATA_FOLDER, 'config.ini')
    config.read(CONFIG_PATH)

    # Read the token information and start the bot
    token = config['authorization']['token']
    client.run(token)
