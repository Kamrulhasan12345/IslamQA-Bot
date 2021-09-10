import os
import random
import discord

from discord.ext import commands

from scrapSite import fetchQuest, fetchTitle, fetchCategories, fetchImportantTopics, fetchArticles, fetchArticle
from config import TOKEN


bot = commands.Bot(command_prefix='!iqa ')


@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching,
                                name="!iqa help | Assalamu'Alaikum wa rahmatullahi wa barakatuh")
    await bot.change_presence(activity=activity)
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='search', help='Generate search link.')
async def search(ctx, lang_code: str, search_query: str):
    url = "https://islamqa.info/{}/search?q={}&search_engine=website".format(
        lang_code, search_query)
    embed = discord.Embed(title="View search results",
                          url=url, color=discord.Colour(12443287))
    await ctx.send(embed=embed)


@bot.command(name='answer', help='Fetch a specific answer via its question id.')
async def answer(ctx, lang_code: str, question_id: int):
    url = "https://islamqa.info/{}/answers/{}".format(lang_code, question_id)
    description = await fetchQuest(url)
    title = await fetchTitle(url)
    if description != "...":
        embed = discord.Embed(
            title=title, url=url, description=description, color=discord.Colour(12443287))
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=title, url=url, description="Empty", color=discord.Colour(12443287))
        await ctx.send(embed=embed)


@bot.command(name='answers', help='Fetch new answers')
async def answers(ctx, lang_code: str = "en"):
    url = "https://islamqa.info/{}/latest".format(lang_code)
    heads = await fetchCategories(url)
    title = heads[-1]
    embed = discord.Embed(title=title, url=url, color=discord.Colour(12443287))
    if len(heads) == 1:
        embed.add_field(name="\u200b", value="Empty", inline=False)
        await ctx.send(embed=embed)
    elif len(heads) >= 2:
        if len(heads) <= 4:
            for tuple_ in heads[0:len(heads) - 1]:
                embed.add_field(name="\u200b", value="[{}]({})".format(
                    tuple_[0], tuple_[1]), inline=False)
        else:
            for tuple_ in heads[0:5]:
                embed.add_field(name="\u200b", value="[{}]({})".format(
                    tuple_[0], tuple_[1]), inline=False)
        await ctx.send(embed=embed)


@bot.command(name='important_topics', help='Fetch important topics of recent time')
async def important_topics(ctx, lang_code: str = "en"):
    url = "https://islamqa.info/{}".format(lang_code)
    heads = await fetchImportantTopics(url)
    title = heads[-1]
    value = "[{}]({})\n\n[{}]({})\n\n[{}]({})\n\n[{}]({})".format(heads[0][0], heads[0]
                                                                  [1], heads[1][0], heads[1][1], heads[2][0], heads[2][1], heads[3][0], heads[3][1])
    embed = discord.Embed(title=title, url=url, color=discord.Colour(12443287))
    embed.add_field(name="\u200b", value=value, inline=False)
    await ctx.send(embed=embed)


@bot.command(name='articles', help='Fetch new articles')
async def articles(ctx, lang_code: str = "en"):
    url = "https://islamqa.info/{}/articles".format(lang_code)
    heads = await fetchArticles(url)
    title = heads[-1]
    embed = discord.Embed(title=title, url=url, color=discord.Colour(12443287))
    if len(heads) == 1:
        embed.add_field(name="\u200b", value="Empty", inline=False)
        await ctx.send(embed=embed)
    elif len(heads) >= 2:
        if len(heads) <= 4:
            for tuple_ in heads[0:len(heads) - 1]:
                embed.add_field(name="\u200b", value="[{}]({})".format(
                    tuple_[0], tuple_[1]), inline=False)
        else:
            for tuple_ in heads[0:5]:
                embed.add_field(name="\u200b", value="[{}]({})".format(
                    tuple_[0], tuple_[1]), inline=False)
        await ctx.send(embed=embed)


@bot.command(name='article', help='Fetch a specific article via its article id.')
async def article(ctx, lang_code: str, article_id: int):
    url = "https://islamqa.info/{}/articles/{}".format(lang_code, article_id)
    description = await fetchArticle(url)
    title = await fetchTitle(url)
    if description != "...":
        embed = discord.Embed(
            title=title, url=url, description=description, color=discord.Colour(12443287))
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=title, url=url, description="Empty", color=discord.Colour(12443287))
        await ctx.send(embed=embed)


@bot.command(name='category', help='Fetch answers of a specific category (t = topics, vi = very_important, s = selected')
async def categories(ctx, lang_code: str, cat_type: str, category_id: int):
    category_type = "topics" if cat_type == "t" else "very-important" if cat_type == "vi" else "selected" if cat_type == "s" else "topics"
    url = "https://islamqa.info/{}/categories/{}/{}".format(
        lang_code, category_type, category_id)
    heads = await fetchCategories(url)
    title = heads[-1]
    embed = discord.Embed(title=title, url=url, color=discord.Colour(12443287))
    if len(heads) == 1:
        embed.add_field(name="\u200b", value="Empty", inline=False)
        await ctx.send(embed=embed)
    elif len(heads) >= 2:
        if len(heads) <= 4:
            for tuple_ in heads[0:len(heads) - 1]:
                embed.add_field(name="\u200b", value="[{}]({})".format(
                    tuple_[0], tuple_[1]), inline=False)
        else:
            for tuple_ in heads[0:5]:
                embed.add_field(name="\u200b", value="[{}]({})".format(
                    tuple_[0], tuple_[1]), inline=False)
        await ctx.send(embed=embed)


# aliver()
bot.run(TOKEN)
