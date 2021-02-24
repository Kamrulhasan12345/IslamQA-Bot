import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv
from scrapSite import fetchQuest

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!iqa ')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='search', help='Generate search link.')
async def search(ctx, lang_code: str, search_query: str):
    url = "https://islamqa.info/{}/search?q={}&search_engine=website".format(lang_code, search_query)
    embed=discord.Embed(title="View search results", url=url, color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.command(name='fetch', help='Fetch an answer via its question id.')
async def fetch(ctx, lang_code: str, question_id: int):
    url = "https://islamqa.info/{}/answers/{}".format(lang_code, question_id)
    description = await fetchQuest(url)
    embed=discord.Embed(title="Test", url=url, description=description, color=discord.Color.blue())
    await ctx.send(embed=embed)

bot.run(TOKEN)