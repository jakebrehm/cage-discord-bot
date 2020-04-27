import configparser
import discord
import os
import praw
from discord.ext import commands


class Web(commands.Cog):

    def __init__(self, client):
        self.client = client

        CONFIG_PATH = os.path.join('..', 'data', 'config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_PATH)

        self.reddit = praw.Reddit(
            client_id=self.config['reddit']['client id'],
            client_secret=self.config['reddit']['client secret'],
            user_agent=self.config['reddit']['user agent'],
        )

    @commands.command(
        aliases=['top', 'top-post', 'topreddit', 'top-reddit'],
        brief='Get a link to the current top /r/onetruegod post',
    )
    async def toppost(self, context):
        top_posts = self.reddit.subreddit('onetruegod').hot(limit=3)
        for post in top_posts:
            if not post.stickied:
                await context.send(f'https://www.reddit.com{post.permalink}')
                return


def setup(client):
    client.add_cog(Web(client))