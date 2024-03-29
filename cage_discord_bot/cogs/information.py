import discord
from discord.ext import commands


class Information(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
        aliases=['funfact', 'fun-fact'],
        brief='Get a fun fact about our lord and savior',
    )
    async def fact(self, context):
        guild_id = context.guild.id
        database = self.client.database
        await context.send(database.get_random_fact(guild_id))

    @commands.group(
        brief='Get user counts, server counts, and more'
    )
    async def count(self, context):
        if context.invoked_subcommand is None:
            database = self.client.database
            mention = context.author.mention
            await context.send(database[31].format(name=mention))

    @count.command(name='facts')
    async def fact_count(self, context):
        guild_id = context.guild.id
        database = self.client.database
        fact_count = database.get_fact_count(guild_id)
        fact_count_total = database.get_fact_count(guild_id, total=True)
        await context.send(database[28].format(
            guild_facts=fact_count,
            total_facts=fact_count_total,
        ))

    @count.command(name='users')
    async def user_count(self, context):
        guild_id = context.guild.id
        database = self.client.database
        user_count = database.get_user_count(guild_id)
        user_count_total = database.get_user_count(guild_id, total=True)
        await context.send(database[29].format(
            guild_users=user_count,
            total_users=user_count_total,
        ))

    @count.command(name='servers')
    async def server_count(self, context):
        guild_id = context.guild.id
        database = self.client.database
        server_count = len(self.client.guilds)
        await context.send(database[30].format(total_servers=server_count))


async def setup(client):
    await client.add_cog(Information(client))