#Seagull By Seabear & Rag3

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from itertools import cycle

bot = commands.Bot(command_prefix='-')
status = ['Online in 1 server']

@bot.event
async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(status)

    while not bot.is_closed:
        current_status = next(msgs)
        await bot.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(5)

@bot.event
async def on_ready():
    print ("Starting... Done!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here Is The Server Info:", color=0x00ff00)
    embed.set_author(name="Rag3 & Seabear")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def commands(ctx):
    await bot.say("serverinfo, info, ping. More Coming soon :)")   

@bot.command(pass_context=True)
async def kick(ctx, member: discord.Member):
    await bot.kick(member)

@bot.command(pass_context=True)
async def ban(ctx, member: discord.Member):
    await bot.ban(member)
    await bot.say('Banned {0}'.format(member.mention))
    
@bot.command() 
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await bot.say(output) 

@bot.command(pass_context=True)
async def purge(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say('Messages Deleted')    

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name = 'User')
    await bot.add_roles(member, role)

@bot.command(pass_context=True)
async def suggest(ctx, *suggestion):
    channel = discord.utils.get(ctx.message.author.server.channels, name="suggestions")
    embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            colour=discord.Colour.gold()
    )
    embed.add_field(name="New suggestions", value="{0}".format(' '.join(suggestion)))
    embed.set_footer(text="Bot created by: Rag3#4930")
    message = await bot.send_message(channel, embed=embed)
    await bot.add_reaction(message, "?")
    await bot.add_reaction(message, "?")


@bot.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await bot.send_message(server, fmt.format(member, server))

    
bot.loop.create_task(change_status())
bot.run("NTI0MDY2MjQ5Mzk1OTI5MTAz.Dviq5A.2sixszdetiEQW56lf4AvS2HxTEs")
