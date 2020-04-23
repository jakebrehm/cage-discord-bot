import discord
import json
import os
import random
from discord.ext import commands

import database as db


class Information(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.DATABASE_LOCATION = os.path.join('..', 'data', 'data.db')

    @commands.command(aliases=['fact', 'fun-fact'])
    async def funfact(self, context):
        database = db.Database(self.DATABASE_LOCATION)
        await context.send(database.random_fact)


def setup(client):
    client.add_cog(Information(client))