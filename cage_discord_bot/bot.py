import asyncio
import configparser
import inspect
import os
import random

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

        self.roles = {}

    async def on_ready(self):
        print('Bot is ready.')
        for guild in self.guilds:
            if guild.name == 'The Cage':
                for role in guild.roles:
                    self.roles[role.name] = {
                        'id': role.id,
                        'role': discord.utils.get(guild.roles, id=role.id),
                    }

    async def on_member_join(self, member):
        print(f'{member} has joined the server.')
        await self.assign_role(member)

    async def on_member_remove(self, member):
        print(f'{member} has left the server.')

    async def load(self, context, extension):
        client.load_extension(f"cogs.{extension}")

    async def unload(self, context, extension):
        client.unload_extension(f"cogs.{extension}")

    async def reload(self, context, extension):
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f"cogs.{extension}")

    async def assign_role(self, user):
        points = self.database.get_points(user)
        if -5 < points < 5:
            await user.remove_roles(self.roles['believer']['role'])
            await user.remove_roles(self.roles['heathen']['role'])
            await user.add_roles(self.roles['neutral']['role'])
        elif points >= 5:
            await user.remove_roles(self.roles['neutral']['role'])
            await user.remove_roles(self.roles['heathen']['role'])
            await user.add_roles(self.roles['believer']['role'])
        elif points <= -5:
            await user.remove_roles(self.roles['neutral']['role'])
            await user.remove_roles(self.roles['believer']['role'])
            await user.add_roles(self.roles['heathen']['role'])

    async def update_user(self, user, points):
        self.database.add_points(user, points)
        await self.assign_role(user)

    async def ping(self, context):
        await context.send(self.database[1].format(name=context.author.mention))

    async def on_command_error(self, context, error):
        mention = context.message.author.mention
        if isinstance(error, commands.CommandNotFound):
            await context.send(self.database[2].format(name=mention))
        elif isinstance(error, commands.MissingPermissions):
            await context.send(self.database[3].format(name=mention))
        else:
            print(error)

    async def on_message(self, message):
        if message.author.bot:
            return
        deformatted = message.content.lower().replace(' ', '')
        name, discriminator = message.author.name, message.author.discriminator
        mention = message.author.mention
        if all(s in deformatted for s in ['who', 'nic', 'cage']):
            await message.channel.send(self.database[4].format(name=mention))
            await asyncio.sleep(2)
            await message.author.kick(reason=f"{name} was being absurd.")
            await asyncio.sleep(1)
            await message.channel.send(self.database[5].format(name=mention))
        if all(s in deformatted for s in ['love', 'nic', 'cage']):
            reactions = ['❤', '💋', '😘']
            await message.add_reaction(random.choice(reactions))
            await self.update_user(message.author, 1)
        await client.process_commands(message)


if __name__ == '__main__':

    # Initialize the client
    DATABASE_LOCATION = os.path.join('..', 'data', 'data.db')
    client = Client(command_prefix='.', database_location=DATABASE_LOCATION)

    # Load the cogs
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f"cogs.{filename[:-3]}")

    # Read the configuration file
    config = configparser.ConfigParser()
    CONFIG_PATH = os.path.join('..', 'data', 'config.ini')
    config.read(CONFIG_PATH)

    # Read the token information and start the bot
    token = config['authorization']['token']
    client.run(token)
