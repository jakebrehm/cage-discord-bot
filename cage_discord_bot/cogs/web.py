import asyncio
import os
import re

import aiohttp
import discord
import praw
from discord.ext import commands


class Web(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.reddit = praw.Reddit(
            client_id=self.client.config['REDDIT_CLIENT_ID'],
            client_secret=self.client.config['REDDIT_CLIENT_SECRET'],
            user_agent=self.client.config['REDDIT_USER_AGENT'],
        )

    @commands.command(
        aliases=['top', 'top-post', 'topreddit', 'top-reddit'],
        brief='Get a link to the current top /r/onetruegod post',
    )
    async def toppost(self, context):
        top_posts = self.reddit.subreddit('onetruegod').hot(limit=3)
        for post in top_posts:
            if not post.stickied:
                title = post.title
                subreddit = post.subreddit_name_prefixed
                score = post.ups + post.downs # post.score
                comments = post.num_comments
                link = f'https://www.reddit.com{post.permalink}'

                embed = discord.Embed(
                    title=f'{subreddit} - {title}',
                    author=post.author,
                    description=f'{score} points and {comments} comments so far on Reddit',
                    url=link,
                )
                embed.set_thumbnail(url=post.thumbnail)

                await context.send(content=None, embed=embed)
                return


    @commands.group(
        brief="Make things such as memes"
    )
    async def make(self, context):
        if context.invoked_subcommand is None:
            database = self.client.database
            mention = context.author.mention
            await context.send(database[21].format(name=mention))

    @make.command(name='meme')
    async def make_meme(self, context, *, template=None):
        database = self.client.database
        mention = context.author.mention

        def check(author):
            def inner_check(message):
                return message.author == author
            return inner_check

        if template is None:
            await context.send(database[22].format(name=mention))
            await context.send(
                'The following templates are available:\n'
                "> 1. You don't say\n"
                "> 2. Cool breeze"
            )
            return

        deformatted = context.message.content.lower().replace(' ', '')
        deformatted = re.sub(r'[^\w\s]', '', deformatted)
        print(deformatted)
        if all(s in deformatted for s in ['cool', 'breeze']):
            template_id = 10369075
        elif all(s in deformatted for s in ['you', 'dont', 'say']):
            template_id = 31836096
        else:
            await context.send(database[26].format(name=mention))
            return

        top_query = await context.send(database[23].format(name=mention))
        try:
            top_response = await self.client.wait_for(
                'message',
                timeout=60,
                check=check(context.author),
            )
        except asyncio.TimeoutError:
            mention = top_response.mention
            await context.send(database[11].format(name=mention))
        else:
            top_text = top_response.content

        bottom_query = await context.send(database[24])
        try:
            bottom_response = await self.client.wait_for(
                'message',
                timeout=60,
                check=check(context.author),
            )
        except asyncio.TimeoutError:
            mention = bottom_response.mention
            await context.send(database[11].format(name=mention))
        else:
            bottom_text = bottom_response.content

        await top_query.delete()
        await bottom_query.delete()
        await top_response.delete()
        await bottom_response.delete()

        url='https://api.imgflip.com/caption_image'
        data = {
            'template_id': template_id,
            'text0': top_text,
            'text1': bottom_text,
            'username': self.client.config['IMGFLIP_USERNAME'],
            'password': self.client.config['IMGFLIP_PASSWORD'],
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, params=data) as response:
                result = await response.json()

        if result['success']:
            await context.send(result['data']['url'])
        else:
            await context.send(database[25].format(name=mention))







def setup(client):
    client.add_cog(Web(client))
