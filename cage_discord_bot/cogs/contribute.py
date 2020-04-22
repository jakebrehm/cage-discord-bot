import discord
import os
from discord.ext import commands

import database as db


class Contribute(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.DATABASE_LOCATION = os.path.join('..', 'data', 'data.db')

    @commands.command(aliases=['remind'])
    async def submit(self, context, which, *, submission):
        if which in ['fact', 'fun-fact']:
            database = db.Database(self.DATABASE_LOCATION)
            database.submit_fact(context.guild.id, context.author.id, 'accepted', submission)
            database.terminate()
            await context.send(
                f"Thanks for reminding me, {context.author.name}. "
                f"I can't believe I forgot."
            )
        else:
            await context.send(
                f"What are you trying to remind me of, {context.author.name}? "
                f"I don't understand."
            )


def setup(client):
    client.add_cog(Contribute(client))
