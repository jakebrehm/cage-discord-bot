import discord
from discord.ext import commands


class Information(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(
        brief='Submit information such as a fact'
    )
    async def fact(self, context):
        if context.invoked_subcommand is None:
            guild_id = context.guild.id
            database = self.client.database
            await context.send(database.get_random_fact(guild_id))

    @fact.command(name='count')
    async def fact_count(self, context):
        guild_id = context.guild.id
        database = self.client.database
        fact_count = database.get_fact_count(guild_id)
        fact_count_total = database.get_fact_count(guild_id, total=True)
        await context.send(f'There are {fact_count} facts for this server, and {fact_count_total} in total.')

    @fact.command(name='users')
    async def user_count(self, context):
        guild_id = context.guild.id
        database = self.client.database
        user_count = database.get_user_count(guild_id)
        user_count_total = database.get_user_count(guild_id, total=True)
        await context.send(f'I am currently tracking points for {user_count} users in this server, and {user_count_total} in total.')

    @fact.command(name='servers')
    async def server_count(self, context):
        guild_id = context.guild.id
        database = self.client.database
        server_count = len(self.client.guilds)
        await context.send(f'I am currently in {server_count} servers.')


def setup(client):
    client.add_cog(Information(client))