import discord
import os
from discord.ext import commands


class Contribute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['remind'])
    async def submit(self, context, which, *, submission):
        guild_id = context.guild.id
        author_name = context.author.name
        author_id = context.author.id
        if which in ['fact', 'fun-fact']:
            database = self.client.database
            database.submit_fact(guild_id, author_id, 'pending', submission)
            database.terminate()
            await context.send(
                f"Thanks for reminding me, {author_name}. "
                f"I can't believe I forgot."
            )
        else:
            await context.send(
                f"What are you trying to remind me of, {author_name}? "
                f"I don't understand."
            )


def setup(client):
    client.add_cog(Contribute(client))
