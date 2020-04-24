import asyncio
import inspect

import discord
from discord.ext import commands

import database as db


class Client(commands.Bot):

    def __init__(self, *args, database_location, **kwargs):

        super().__init__(*args, **kwargs)

        self.database_location = database_location
        self.database = db.Database(self.database_location)

        self.add_command(commands.Command(self.load))
        self.add_command(commands.Command(self.unload))
        self.add_command(commands.Command(self.reload))
        self.add_command(commands.Command(self.ping))

    async def on_ready(self):
        print('Bot is ready.')

    async def load(self, context, extension):
        client.load_extension(f"cogs.{extension}")

    async def unload(self, context, extension):
        client.unload_extension(f"cogs.{extension}")

    async def reload(self, context, extension):
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f"cogs.{extension}")

    async def ping(self, context):
        await context.send("Don't worry, I'm here.")

    async def on_command_error(self, context, error):
        name = context.message.author.name
        if isinstance(error, commands.CommandNotFound):
            await context.send(f"I'm not sure what you're asking me to do, {name}.")
        elif isinstance(error, commands.MissingPermissions):
            await context.send(f"Sorry {name}, I can't let you do that.")
        else:
            print(error)

    async def on_message(self, message):
        deformatted = message.content.lower().replace(' ', '')
        name, discriminator = message.author.name, message.author.discriminator
        if all(s in deformatted for s in ['who', 'nic', 'cage']):
            await message.channel.send(f"That's ridiculous, {name}. Goodbye.")
            await asyncio.sleep(2)
            await message.author.kick(reason=f"{name} was being absurd.")
            await asyncio.sleep(1)
            await message.channel.send("That was ugly. I'm sorry, everyone.")
        if all(s in deformatted for s in ['love', 'nic', 'cage']):
            await message.add_reaction('❤')
        await client.process_commands(message)


if __name__ == '__main__':

    import configparser
    import os

    DATABASE_LOCATION = os.path.join('..', 'data', 'data.db')
    client = Client(command_prefix='.', database_location=DATABASE_LOCATION)

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
