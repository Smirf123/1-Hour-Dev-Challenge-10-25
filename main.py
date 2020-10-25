# main.py built by Smirf123
import discord
import requests
import json
import asyncio
from discord.ext.commands import AutoShardedBot
from discord.ext import commands

TOKEN = ('NzY5NzE5ODA3NjI0ODcxOTg2.X5THbg.ytusiDG0-o7oHewQ-DNvNeo1moY')
client = commands.AutoShardedBot(command_prefix = '?')

guild = discord.Guild

@client.event
async def on_ready():
    print("The bot has connected to Discord and ready to serve")
    print(f"Username: {client.user}")

@client.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    sid = str(ctx.guild.id)
    membercount = str(ctx.guild.member_count)
    await ctx.channel.send(f'The guild is called {name} and has an ID of {sid} and has {membercount} members')
@client.command()
async def whois(ctx, member: discord.Member = None):
    member = ctx.author if not member else member

    await ctx.channel.send(f'This member is {member.mention} with a User ID of {member.id} and joined Discord on {member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}')
@client.command()
async def chat(ctx, meme):
    await ctx.channel.send('Give me a sec while I wake the humans up')
    request = requests.get(f"https://some-random-api.ml/chatbot?message={meme}")
    json_response = request.json()
    message = json_response['response']
    await ctx.channel.send(f'The chatbot says {message}')
@client.command()
async def doggo(ctx):
    request = requests.get("https://some-random-api.ml/img/dog")
    json_response = request.json()
    message = json_response['link']
    await ctx.channel.send(message)
@client.command()
async def catto(ctx):
    request = requests.get("https://some-random-api.ml/img/cat")
    json_response = request.json()
    message = json_response['link']
    await ctx.channel.send(message)

client.run(TOKEN)